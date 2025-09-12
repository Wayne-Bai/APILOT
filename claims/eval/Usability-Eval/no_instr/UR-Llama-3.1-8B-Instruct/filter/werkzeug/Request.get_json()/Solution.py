from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def parse_json():
    try:
        # Attempt to parse the JSON from the request
        data = request.get_json()
        
        # Return the parsed JSON data
        return jsonify(data)
    
    except BadRequest:
        # If there was a problem parsing the JSON, return a 400 error
        return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
