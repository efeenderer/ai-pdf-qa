import os, json
from flask import Flask, request, jsonify, render_template, send_from_directory
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Welcome to the Flask API!"



if __name__ == '__main__':
    app.run(debug=True, port=5000)
