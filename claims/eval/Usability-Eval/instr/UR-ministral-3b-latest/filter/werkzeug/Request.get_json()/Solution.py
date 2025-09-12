from flask import Flask, request
from werkzeug.wrappers import Request

app = Flask(__name__)

@app.route('/parse-json', methods=['POST'])
def parse_json():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
