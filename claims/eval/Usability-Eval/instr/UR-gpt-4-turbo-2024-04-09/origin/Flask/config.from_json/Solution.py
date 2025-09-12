from flask import Flask
import json

app = Flask(__name__)

def load_config_from_json(json_file):
    with open(json_file) as config_file:
        config_data = json.load(config_file)
        app.config.from_mapping(config_data)

# Example usage
if __name__ == "__main__":
    load_config_from_json('config.json')
    app.run()
