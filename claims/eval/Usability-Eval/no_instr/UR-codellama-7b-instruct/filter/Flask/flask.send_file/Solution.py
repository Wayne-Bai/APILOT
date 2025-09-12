
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/download', methods=['GET'])
def download():
    file_path = 'path/to/file'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
