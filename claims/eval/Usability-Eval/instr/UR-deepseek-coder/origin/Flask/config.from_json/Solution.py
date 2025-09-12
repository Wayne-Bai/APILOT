from flask import Flask, json

app = Flask(__name__)

def update_config_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        config_data = json.load(file)
        app.config.update(config_data)

# Example usage
# update_config_from_json('path_to_your_config.json')
