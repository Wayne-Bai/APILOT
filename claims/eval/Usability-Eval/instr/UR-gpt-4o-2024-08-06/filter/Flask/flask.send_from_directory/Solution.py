from flask import Flask, send_file, request, abort
import os

app = Flask(__name__)

# Directory containing files to be sent
FILES_DIRECTORY = '/path/to/your/files'

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_path = os.path.join(FILES_DIRECTORY, filename)
        # Ensure the file exists within the directory
        if os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            abort(404)  # File not found
    except Exception as e:
        abort(500)  # Server error

if __name__ == '__main__':
    app.run(debug=True)
