import json
from flask import Flask, current_app, config

app = Flask(__name__)

def update_config_from_json(file_path):
    with open(file_path, 'r') as file:
        config_dict = json.load(file)
    current_app.config.update(config_dict)
    for key, value in config_dict.items():
        setattr(app.config, key, value)

# Example usage
if __name__ == '__main__':
    update_config_from_json('config.json')
    print(app.config)
