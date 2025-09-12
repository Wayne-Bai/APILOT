from flask import Flask, current_app, request, abort
import json

app = Flask(__name__)

def update_config_from_json(config_file_path):
    with open(config_file_path, 'r') as file:
        json_data = json.load(file)

    with app.app_context():
        current_app.config.update(json_data)

@app.route('/update-config', methods=['POST'])
def update_config():
    if not request.is_json:
        return abort(400, 'Invalid content-type: must be application/json')

    try:
        json_data = request.get_json()
        update_config_from_json(json_data)
        return {'message': 'Config updated successfully'}, 200
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    update_config_from_json('config.json')
    app.run(debug=True)
