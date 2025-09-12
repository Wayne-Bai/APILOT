from flask import Flask, request
from os.path import abspath, join

app = Flask(__name__)

@app.route('/join', methods=['POST'])
def join():
    data = request.get_json()
    base_dir = abspath(data.get('base_dir'))
    path_components = data.get('path_components', [])

    for component in path_components:
        base_dir = join(base_dir, component)

    return {'joined_dir': base_dir}

if __name__ == '__main__':
    app.run()
