from flask import Flask, request, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/files/<path:filename>')
def serve_file(filename):
    # Define the base directory
    base_directory = '/path/to/your/base/directory'

    # Safely join the filename to the base directory
    safe_path = os.path.join(base_directory, os.path.normpath(filename))

    # Ensure the resulting path is within the base directory
    if not safe_path.startswith(os.path.abspath(base_directory)):
        abort(403)  # Forbidden

    # Serve the file if it exists
    if os.path.exists(safe_path) and os.path.isfile(safe_path):
        return send_from_directory(base_directory, filename)
    else:
        abort(404)  # Not Found

if __name__ == '__main__':
    app.run(debug=True)
