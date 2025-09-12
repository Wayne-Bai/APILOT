import os
from flask import Flask, abort

app = Flask(__name__)

BASE_DIR = '/var/www'

@app.route('/<path:path>')
def serve_file(path):
    # Safely join path to base directory
    full_path = os.path.normpath(os.path.join(BASE_DIR, path))

    # Check if the joined path is a subpath of the base directory
    if os.path.commonpath([BASE_DIR]) != os.path.commonpath([BASE_DIR, full_path]):
        # If not, return a 404 error
        abort(404)

    # If yes, serve the file. Replace this with your actual file serving code.
    return 'File content'

if __name__ == '__main__':
    app.run()
