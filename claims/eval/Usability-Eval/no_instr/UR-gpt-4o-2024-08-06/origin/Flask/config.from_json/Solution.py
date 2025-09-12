from flask import Flask, json

app = Flask(__name__)

def update_config(app, json_file_path):
    """Updates the values in the config from a JSON file."""
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            app.config.from_mapping(data)
    except FileNotFoundError:
        print(f"File at {json_file_path} not found.")
    except json.JSONDecodeError:
        print("JSON decode error - check the file for correct JSON format.")

# Example usage
update_config(app, 'config.json')

if __name__ == "__main__":
    app.run(debug=True)
