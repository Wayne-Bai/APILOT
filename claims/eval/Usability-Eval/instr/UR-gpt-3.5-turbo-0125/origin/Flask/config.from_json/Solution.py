
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def update_config_from_json():
    with open('config.json', 'r') as file:
        config_data = json.load(file)
    app.config.from_mapping(config_data)
    return 'Config values updated successfully!'

if __name__ == '__main__':
    app.run()
