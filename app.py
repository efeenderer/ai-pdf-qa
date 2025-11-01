import os, json
from flask import Flask, request, jsonify, render_template, send_from_directory
from dotenv import load_dotenv
load_dotenv()

# Utility functions
from utils import extract_text_from_pdf

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    pass # To be implemented





if __name__ == '__main__':
    app.run(debug=True, port=5000)
