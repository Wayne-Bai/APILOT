from flask import Flask
import json

app = Flask(__name__)

def update_config_from_file(file_path):
    with open(file_path) as config_file:
        config_data = json.load(config_file)
        app.config.from_mapping(config_data)
