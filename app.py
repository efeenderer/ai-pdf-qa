import os, json
from flask import Flask, request, jsonify, render_template, send_from_directory
from dotenv import load_dotenv
load_dotenv()

import pdfplumber
pdf_path = os.getenv("PDF_FOLDER")
def extract_text_from_pdf(file_path):
    texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            texts.append(page.extract_text())
    return texts

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("pdfs")
    file_texts = []
    for file in uploaded_files:
        if file.filename.endswith('.pdf'):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            texts = extract_text_from_pdf(file_path)
            file_texts.append({'filename': file.filename, 'text': texts})
    return jsonify({'files': file_texts})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
