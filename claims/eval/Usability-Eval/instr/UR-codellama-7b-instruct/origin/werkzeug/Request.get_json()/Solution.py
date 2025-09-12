
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def parse_json_request():
    json_data = request.get_json()
    return jsonify(json_data)
