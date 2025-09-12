
from flask import jsonify, request
from myproject.config import Config

def update_config_from_json(filepath):
    with open(filepath) as f:
        data = json.load(f)
    config = Config.from_mapping(data)
    return config

@app.route('/update_config', methods=['POST'])
def update_config():
    filepath = request.form['filepath']
    new_config = update_config_from_json(filepath)
    return jsonify({'message': 'Config updated successfully!'})
