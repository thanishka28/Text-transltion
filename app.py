from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

# Update the Tesseract path (required on Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

translator = Translator()

# Function to extract text from an image
def extract_text(image_path):
    try:
        image = Image.open(image_path)  # Open the image using PIL
        text = pytesseract.image_to_string(image)  # Extract text using Tesseract
        return text.strip()  # Return extracted text (remove extra spaces/new lines)
    except Exception as e:
        return str(e)  # Return error message

@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    target_lang = data.get('language')

    if not text or not target_lang:
        return jsonify({'error': 'Missing text or target language'}), 400

    try:
        translated = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/extract-text', methods=['POST'])
def extract_text_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    image_path = "uploaded_image.png"
    image.save(image_path)  # Save uploaded image to disk

    print("✅ Image received:", image.filename) #debugging log

    try:
        # Open image & extract text
        extracted_text = pytesseract.image_to_string(Image.open(image_path))
        print("📝 Extracted text:", extracted_text)  # Debugging log

        if not extracted_text.strip():
            return jsonify({'error': 'No text found in image'}), 400  # Handle empty output

        return jsonify({'extracted_text': extracted_text})

    except Exception as e:
        print("❌ Error:", str(e))  # Debugging log
        return jsonify({'error': str(e)}), 500

@app.route('/translate-extracted-text', methods=['POST'])
def translate_extracted_text():
    data = request.json
    text = data.get('text')
    target_lang = data.get('language')

    if not text or not target_lang:
        return jsonify({'error': 'Missing text or target language'}), 400

    try:
        translated = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 5000)