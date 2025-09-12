from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/update_config', methods=['POST'])
def update_config():
    data = request.get_json()
    if 'config' in data:
        config = data['config']
        app.config.update(config)
        return jsonify({'message': 'Config updated successfully'}), 200
    else:
        return jsonify({'message': 'Invalid config data'}), 400

if __name__ == '__main__':
    app.run()
