import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/config', methods=['PUT'])
def update_config():
    data = json.loads(request.data)
    app.config.from_mapping(data)
    return jsonify({'message': 'Config updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
