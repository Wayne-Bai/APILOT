from flask import Flask, request
from werkzeug.utils import safe_join

app = Flask(__name__)

@app.route('/join', methods=['GET'])
def safe_file_join():
    base_directory = request.args.get('base_directory', '')
    paths = request.args.get('paths', '').split(',')
    return safe_join(base_directory, *paths)

if __name__ == '__main__':
    app.run(debug=True)
