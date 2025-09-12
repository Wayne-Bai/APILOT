from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/upload/<path:filename>')
def send_file_from_directory(filename):
    # Ensure the file exists in the specified directory
    file_path = os.path.join('path_to_your_directory', filename)
    if not os.path.isfile(file_path):
        return "File not found", 404

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
