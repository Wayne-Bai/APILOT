import json
from flask import Flask

app = Flask(__name__)

def update_config_from_json(json_file):
    with open(json_file) as f:
        config_data = json.load(f)
    app.config.update(config_data)

# Usage
update_config_from_json('config.json')
