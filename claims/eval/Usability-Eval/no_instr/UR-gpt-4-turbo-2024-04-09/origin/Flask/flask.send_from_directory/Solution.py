from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    path = "path/to/your/file.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run()
