from flask import Flask, abort, request
import os

app = Flask(__name__)

@app.route('/files/<path:filename>')
def download_file(filename):
    # Define the base directory
    base_directory = '/path/to/secure/base/directory'

    # Safely join the filename with the base directory
    full_path = os.path.normpath(os.path.join(base_directory, filename))

    # Ensure that the resulting path is inside the base directory
    if os.path.commonpath([base_directory]) != os.path.commonpath([base_directory, full_path]):
        abort(403)  # Forbidden

    # Now you can safely serve the file from full_path
    try:
        with open(full_path, 'rb') as file:
            file_data = file.read()
            return file_data, 200, {'Content-Type': 'application/octet-stream'}
    except FileNotFoundError:
        abort(404)  # Not Found

if __name__ == '__main__':
    app.run(debug=True)
