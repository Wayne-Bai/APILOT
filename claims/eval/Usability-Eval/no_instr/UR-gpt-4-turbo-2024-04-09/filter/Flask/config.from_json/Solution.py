from flask import Flask
import json

app = Flask(__name__)

def update_config_from_json(json_file):
    with open(json_file, 'r') as f:
        config_data = json.load(f)
    app.config.from_mapping(config_data)

# Example usage
if __name__ == "__main__":
    update_config_from_json('config.json')
    app.run(debug=True)
