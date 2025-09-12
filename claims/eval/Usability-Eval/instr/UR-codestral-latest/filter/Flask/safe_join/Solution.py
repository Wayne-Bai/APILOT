from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/join_path', methods=['GET'])
def join_path():
    base_dir = '/base/directory'
    path_components = request.args.getlist('components')

    full_path = base_dir
    for component in path_components:
        full_path = os.path.join(full_path, component)

    return full_path, 200

if __name__ == '__main__':
    app.run(debug=True)
