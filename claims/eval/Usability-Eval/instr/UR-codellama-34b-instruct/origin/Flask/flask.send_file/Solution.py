
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/send-file", methods=["GET"])
def send_file():
    filepath = "path/to/your/file"
    return send_file(filepath, mimetype="text/plain")
