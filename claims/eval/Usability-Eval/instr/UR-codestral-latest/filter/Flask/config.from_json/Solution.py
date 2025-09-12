from flask import Flask, json

app = Flask(__name__)

class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def from_mapping(self, mapping):
        for key, value in mapping.items():
            setattr(self, key, value)

@app.route('/update_config', methods=['GET'])
def update_config():
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    config = Config()
    config.from_mapping(config_data)

    # Use the config as needed...

    return 'Configuration updated successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
