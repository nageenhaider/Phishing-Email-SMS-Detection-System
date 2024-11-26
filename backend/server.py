# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from app.utils import clean_text
import os
import pdfplumber

app = Flask(__name__)

# Enable CORS for the React app running on localhost:3000
CORS(app)

UPLOAD_FOLDER = 'uploadedfiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


model = joblib.load('app/models/sms_model.pkl')
vectorizer = joblib.load('app/models/sms_vectorizer.pkl')

model_email = joblib.load('app/models/phishing_email_model_3.pkl')
vectorizer_email = joblib.load('app/models/tfidf_vectorizer_3.pkl')

# Route to scan SMS
@app.route('/scan-sms', methods=['POST'])
def scan_sms():
    data = request.json.get('sms', '')
    if not data:
        return jsonify({"error": "No SMS text provided"}), 400

    cleaned_sms = clean_text(data)
    sms_vector = vectorizer.transform([cleaned_sms])

    prediction = model.predict(sms_vector)
    result = "spam" if prediction[0] == 1 else "ham"

    return jsonify({"prediction": result})


@app.route('/emailscan', methods=['POST'])
def predict():
    try:
        email = request.json['body']
        print(email)
        if not email:
            return jsonify({'error': 'No email provided'}), 400

        cleaned_email = clean_text(email)
        email_vector = vectorizer_email.transform([cleaned_email])
        prediction_email = model_email.predict(email_vector)
        print(prediction_email)
        result1 = "spam" if prediction_email[0] == 1 else "ham"
        return jsonify({'prediction': result1})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/uploadattachment', methods=['POST'])
def handle_attachment():
    if 'attachment' in request.files:
        file = request.files['attachment']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        
        file.save(file_path)
        try:
            if file.filename.endswith('.pdf'):
                with pdfplumber.open(file_path) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text()

                # Clean the extracted text
                cleaned_text = clean_text(text)

                # Vectorize the cleaned text for phishing detection
                email_vector = vectorizer_email.transform([cleaned_text])

                # Predict if the text is phishing or not
                prediction_email = model_email.predict(email_vector)
                result = "spam" if prediction_email == "Phishing Email" else "ham"

                return jsonify({
                    "message": "PDF attachment uploaded and parsed successfully",
                    "text": text,
                    "prediction": result
                })
            else:
                return jsonify({"error": "Unsupported file type. Only PDF files are supported"}), 400

        except Exception as e:
            return jsonify({"error": f"Failed to parse the file: {str(e)}"}), 500

    return {"error": "No attachment found"}, 400


if __name__ == '__main__':
    app.run(debug=True)

