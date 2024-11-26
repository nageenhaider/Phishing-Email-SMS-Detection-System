import re

def clean_text(text):
    """Clean the input SMS text."""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\W", " ", text)  # Remove non-alphanumeric characters
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.strip()
