from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/<path:filename>')
def download_file(filename):
    # Safely join the base directory and the filename
    safe_filename = os.path.join('/path/to/base/directory', filename)
    
    # Check if the resulting path is within the base directory
    if os.path.isabs(safe_filename) and safe_filename.startswith('/path/to/base/directory'):
        # Serve the file from the safe path
        return send_from_directory('/path/to/base/directory', filename)
    else:
        # Return an error if the resulting path is outside the base directory
        return 'Error: Path is outside the base directory', 403
