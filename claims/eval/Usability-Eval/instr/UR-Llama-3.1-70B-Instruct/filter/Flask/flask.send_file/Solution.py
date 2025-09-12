
from flask import Flask, send_from_directory, safe_join

app = Flask(__name__)

# Define the path to the directory containing the files
DIRECTORY_PATH = './files'

@app.route('/download/<filename>')
def download_file(filename):
    # Use send_from_directory to send the file contents to the client
    return send_from_directory(directory=DIRECTORY_PATH, path=safe_join(DIRECTORY_PATH, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
