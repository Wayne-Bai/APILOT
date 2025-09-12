
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    filename = 'example_file.txt'
    return send_file(filename)

if __name__ == '__main__':
    app.run()
