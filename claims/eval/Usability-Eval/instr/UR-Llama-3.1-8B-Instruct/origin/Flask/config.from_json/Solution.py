from flask import Flask, json
from flask import request
from config import Config  # Assuming you have a config file

app = Flask(__name__)
app.config.from_object(Config)

def update_config_from_json(app):
    json_data = request.get_json()
    
    if json_data is None:
        return "Missing JSON data", 400
    
    try:
        app.config.from_mapping(json_data)
    except Exception as e:
        return f"Failed to update config: {e}", 500
    
    return "Config updated successfully", 200

# Update values config from a JSON file
@app.route('/update_config', methods=['POST'])
def update_config():
    return update_config_from_json(app)

if __name__ == "__main__":
    app.run(debug=True)
