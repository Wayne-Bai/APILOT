
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the base directory from the URL
    base_directory = os.path.dirname(request.url)
    
    # Get the untrusted path components from the query string
    untrusted_path = request.args.get('path', '')
    
    # Join the untrusted path components to the base directory
    safe_path = os.path.join(base_directory, untrusted_path)
    
    # Check if the safe path is within the base directory
    if not os.path.commonprefix([safe_path, base_directory]):
        return 'The requested path is outside of the base directory', 403
    
    # Return the safe path
    return safe_path
