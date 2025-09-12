from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/update_config', methods=['POST'])
def update_config():
    data = json.loads(request.data)
    config = app.config.from_mapping(data)
    return jsonify(config)

if __name__ == '__main__':
    app.run()
