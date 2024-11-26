Phishing Detection System
This project is a phishing detection system that analyzes emails, attachments, and SMS messages to identify potential phishing threats. The system leverages machine learning models for real-time predictions.
Features
* Scan Email: Enter the email subject, body, and upload attachments to detect phishing threats.
* Scan SMS: Submit SMS text to identify spam messages.
* Scan Attachment: Upload files to analyze their content for potential phishing.
* History: View a record of previously scanned items with results.


Prerequisites
* Backend:
   * Python 3.8 or higher
   * pip (Python package manager)
* Frontend:
   * Node.js 16 or higher
   * npm (Node Package Manager)


File Structure
/project-root
  ├── frontend/                  
  │          ├── public/                  # Static assets
  │          ├── src/                      # Frontend code
  │          ├── components/       # Shared React components
  │          ├── pages/                 # Individual page components
  │          ├── styles/                 # CSS files
  │          └── App.js                 # Main React component
  ├── backend/                        # Backend code
  │   ├── app/          
  │        ├── models/                #ML models
  │             ├──phishing_email_model_3.pkl
  │             ├──sms_model.pkl
  │             ├──sms_vectorizer.pkl
  │             ├──tfidf_vectorizer_3.pkl
  │   ├── uploadedfiles/           # Folder where attachments will be uploaded
  │   ├── server.py                   # Entry point of backend. Contains all API endpoints
  │   ├── requirements.txt
  └── README.md                 # Documentation




Installation and Setup
1. Clone the Repository
git clone https://github.com/your-username/phishing-detection.git
cd phishing-detection


2. Backend Setup
Navigate to the backend folder:
cd backend
1. Install dependencies:
pip install -r requirements.txt
2. Start the backend server:
python server.py
3. The server will run on http://127.0.0.1:5000.
3. Frontend Setup
Navigate back to the project root:
cd ..
   1. Install frontend dependencies:
npm install
   2. Start the React development server:
npm start
   3. The frontend will run on http://localhost:3000.


Usage
1. Scan Email
      * Navigate to the Scan Email page.
      * Enter the subject, body, and upload an attachment.
      * Click Scan to analyze the email for phishing threats.
2. Scan SMS
      * Navigate to the Scan SMS page.
      * Enter the SMS text and click Scan to detect spam.
3. Scan Attachment
      * Navigate to the Scan Attachment page.
      * Upload a file and click Scan to analyze the content.
4. History
      * View previously scanned items on the History page.


API Endpoints
      1. Scan Email:
      * URL: /scan-email
      * Method: POST


      2. Scan SMS:
      * URL: /scan-sms
      * Method: POST


      3. Scan Attachment:
      * URL: /uploadattachment
      * Method: POST
      * Body: Base64-encoded file content.


Troubleshooting
      * CORS Issues: Ensure Flask-CORS is installed and enabled in the backend.
      * Port Conflicts: If ports 3000 or 5000 are in use, modify them in the React or Flask configuration.
      * Dataset Errors: Ensure datasets (sms_spam.csv, email datasets) are present in the backend folder.


   Future Enhancements
      * Deploy on a cloud platform for production use.
      * Add real-time scanning for live email servers.
      * Enhance attachment analysis with deeper content inspection.
