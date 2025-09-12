from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

def safe_join(base_dir, *paths):
    """
    Safely join zero or more untrusted path components to a base directory
    to avoid escaping the base directory.
    """
    full_path = os.path.abspath(os.path.join(base_dir, *paths))
    if not full_path.startswith(os.path.abspath(base_dir)):
        raise ValueError("Attempted to access path outside base directory")
    return full_path

@app.route('/files/<path:filename>')
def serve_file(filename):
    base_dir = '/path/to/base/directory'  # Replace with your base directory
    try:
        full_path = safe_join(base_dir, filename)
        return send_from_directory(base_dir, os.path.relpath(full_path, base_dir))
    except ValueError as e:
        return str(e), 403

if __name__ == '__main__':
    app.run(debug=True)
