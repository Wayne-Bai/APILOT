from flask import Flask, json

app = Flask(__name__)

def update_config_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        config_data = json.load(file)
        app.config.update(config_data)

# Example usage
if __name__ == '__main__':
    update_config_from_json('config.json')
    app.run(debug=True)
