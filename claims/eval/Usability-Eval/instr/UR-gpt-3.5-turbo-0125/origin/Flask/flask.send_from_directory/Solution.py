
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/download")
def download_file():
    filename = "file_to_send.txt"
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run()
