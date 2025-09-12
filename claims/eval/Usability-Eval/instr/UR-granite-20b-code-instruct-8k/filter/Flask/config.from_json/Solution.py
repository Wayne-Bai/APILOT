from flask import Flask
import json

app = Flask(__name__)

@app.route('/update_config', methods=['POST'])
def update_config():
    config_data = request.get_json()
    app.config.from_mapping(config_data)
    return 'Config updated successfully'

if __name__ == '__main__':
    app.run()
