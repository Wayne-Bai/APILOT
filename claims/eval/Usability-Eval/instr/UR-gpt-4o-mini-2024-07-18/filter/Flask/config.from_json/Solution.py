from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Configuration dictionary to hold the current configuration
config = {}

@app.route('/update-config', methods=['POST'])
def update_config():
    global config
    try:
        # Load the JSON data from the request
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON format. Expected a JSON object."}), 400
        
        # Update the config dictionary with the new values
        config.update(data)
        
        return jsonify({"message": "Configuration updated successfully!", "config": config}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
