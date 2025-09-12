from flask import Flask, request, abort
import os

app = Flask(__name__)

def safe_join(base_directory, *paths):
    final_path = os.path.join(base_directory, *paths)
    if not final_path.startswith(os.path.abspath(base_directory)):
        abort(403)  # Forbidden if the path escapes the base directory
    return final_path

@app.route('/files/<path:subpath>')
def serve_file(subpath):
    base_directory = '/path/to/base/directory'
    safe_path = safe_join(base_directory, subpath)
    
    # Here you can add logic to serve the file or directory
    return f"Safe path: {safe_path}"

if __name__ == '__main__':
    app.run()
