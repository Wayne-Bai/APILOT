from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Update the configuration from a JSON file
def update_config_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            import json
            config_dict = json.load(json_file)
            app.config.from_mapping(config_dict)
    except FileNotFoundError:
        print("The JSON file was not found.")
    except json.JSONDecodeError:
        print("The JSON file is not in a valid format.")

# Call the function
update_config_from_json('config.json')

# Example route to test the updated configuration
@app.route('/config', methods=['GET'])
def get_config():
    return jsonify(dict(app.config))

if __name__ == '__main__':
    app.run(debug=True)
