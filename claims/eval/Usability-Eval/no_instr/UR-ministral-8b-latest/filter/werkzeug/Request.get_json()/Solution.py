from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_json():
    if not request.is_json:
        raise BadRequest('Invalid request, expected JSON data.')

    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
