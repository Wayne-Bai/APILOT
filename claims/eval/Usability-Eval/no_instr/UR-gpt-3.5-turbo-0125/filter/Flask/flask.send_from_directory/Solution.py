
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download_file')
def download_file():
    file_path = '/path/to/your/file.txt'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
