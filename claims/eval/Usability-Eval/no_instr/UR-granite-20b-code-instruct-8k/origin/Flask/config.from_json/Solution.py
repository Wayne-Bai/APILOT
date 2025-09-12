
from flask import Flask,json

def update_config_from_json(app: Flask, json_file: str):
    with open(json_file, 'r') as f:
        config = json.load(f)
        app.config.from_mapping(config)
