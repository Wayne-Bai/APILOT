
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/update-config', methods=['POST'])
def update_config():
    config = request.get_json()
    for key, value in config.items():
        if key == 'PORT':
            app.config[key] = value
        elif key == 'DEBUG':
            app.config[key] = bool(value)
    return '', 204
