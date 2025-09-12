from flask import Flask
import os

app = Flask(__name__)

@app.route('/safe-path/<path:subpath>')
def safe_join(subpath):
    base_directory = "/safe/base/directory"
    safe_path = os.path.join(base_directory, subpath)
    # Ensure the path is within the base directory
    safe_path = os.path.normpath(safe_path)
    if not safe_path.startswith(base_directory):
        return "Access denied", 403
    return f"Safe path resolved: {safe_path}"

if __name__ == '__main__':
    app.run(debug=True)
