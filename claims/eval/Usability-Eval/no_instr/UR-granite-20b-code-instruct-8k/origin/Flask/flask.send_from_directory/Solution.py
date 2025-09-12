from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download')
def download_file():
    return send_file('path/to/your/file', as_attachment=True)

if __name__ == '__main__':
    app.run()
