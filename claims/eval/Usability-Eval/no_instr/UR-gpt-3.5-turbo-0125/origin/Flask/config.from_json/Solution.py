
from flask import Flask
import json

app = Flask(__name__)

def update_config_from_json(app, config_file):
    with open(config_file, 'r') as file:
        data = json.load(file)
    app.config.from_mapping(data)

update_config_from_json(app, 'config.json')
