from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route('/send_file', methods=['GET'])
def send_file_route():
    file_path = 'path/to/directory/filename.ext'
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
