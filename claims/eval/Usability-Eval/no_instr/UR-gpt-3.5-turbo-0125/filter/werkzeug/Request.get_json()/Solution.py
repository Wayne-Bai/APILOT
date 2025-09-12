
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/parse_json', methods=['POST'])
def parse_json():
    if request.method == 'POST':
        data = request.get_json()
        return json.dumps(data)

if __name__ == '__main__':
    app.run()
