
from flask import Flask

def update_config_from_json(app, json_file):
    with open(json_file, 'r') as f:
        config = json.load(f)
    app.config.from_mapping(config)
