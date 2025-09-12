from flask import Flask, config

def update_config_from_json(flask_app, json_file_path):
    """
    Updates the values in the config from a JSON file.
    
    This function behaves as if the JSON object was a dictionary and passed to the from_mapping() function.

    :param flask_app: Flask application instance
    :param json_file_path: Path to the JSON file to update the config from
    """
    import json

    try:
        with open(json_file_path, 'r') as json_file:
            json_config = json.load(json_file)
            flask_app.config.from_mapping(json_config)
    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")

# Example usage:
app = Flask(__name__)
update_config_from_json(app, 'config.json')
print(app.config)
