from flask import Flask, request, safe_join, abort
import os

app = Flask(__name__)

@app.route('/files/<path:subpath>', methods=['GET'])
def get_file(subpath):
    base_directory = '/secure/base/directory'  # Change this to your base directory
    safe_path = safe_join(base_directory, subpath)

    # Check if the safe path is still within the base directory
    if not safe_path.startswith(os.path.abspath(base_directory)):
        abort(403)  # Forbidden if the path escapes the base directory

    # Proceed with file handling (reading, returning data, etc.)
    # Example: return the file as a response
    if os.path.isfile(safe_path):
        return send_file(safe_path)  # Ensure to import send_file if used
    else:
        abort(404)  # Not found if the file does not exist

if __name__ == '__main__':
    app.run(debug=True)
