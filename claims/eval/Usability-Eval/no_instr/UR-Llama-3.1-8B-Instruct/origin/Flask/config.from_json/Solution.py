from flask import Flask, request
from flask.config import Config

# Create a Flask app
app = Flask(__name__)

# Update the config from a JSON file
def update_config_from_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    for key, value in data.items():
        app.config[key] = value

# Function to load config from dictionary
def load_config_from_mapping(config_mapping):
    for key, value in config_mapping.items():
        app.config[key] = value

# Route to test the update_config_from_json function
@app.route('/update_config', methods=['POST'])
def update_config():
    if request.method == 'POST':
        json_path = request.form.get('json_path')
        load_config_from_mapping(update_config_from_json(json_path))
        return "Config updated successfully"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
