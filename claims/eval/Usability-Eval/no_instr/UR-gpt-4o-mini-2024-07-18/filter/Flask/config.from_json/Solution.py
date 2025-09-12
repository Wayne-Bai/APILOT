from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Sample config dictionary
config = {}

def update_config_from_json(json_data):
    """Updates the config dictionary from a JSON object."""
    global config
    config.update(json_data)

@app.route('/update-config', methods=['POST'])
def update_config():
    """Endpoint to update the config from a JSON file."""
    if request.is_json:
        json_data = request.get_json()
        update_config_from_json(json_data)
        return jsonify({"message": "Config updated successfully", "config": config}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
