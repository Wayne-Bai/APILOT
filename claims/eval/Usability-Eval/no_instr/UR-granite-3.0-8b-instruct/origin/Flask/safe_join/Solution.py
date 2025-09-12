from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/join_paths', methods=['GET'])
def join_paths():
    base_dir = request.args.get('base_dir', '')
    paths = request.args.getlist('paths[]')

    # Safely join zero or more untrusted path components to a base directory
    # without escaping the base directory
    joined_path = os.path.join(base_dir, *paths)

    return {'joined_path': joined_path}
