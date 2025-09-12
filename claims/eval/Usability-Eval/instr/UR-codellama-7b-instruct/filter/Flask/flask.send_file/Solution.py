
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/send-file')
def send_file():
    # path to the file you want to send
    file_path = 'path/to/your/file.txt'
    return send_file(file_path, mimetype='text/plain')
