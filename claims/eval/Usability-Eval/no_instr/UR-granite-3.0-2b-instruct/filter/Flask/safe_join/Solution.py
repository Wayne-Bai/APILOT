from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/join_paths', methods=['POST'])
def join_paths():
    data = request.get_json()
    base_dir = data.get('base_dir')
    path_components = data.get('path_components', [])

    joined_path = '/' + '/'.join(path_components + [base_dir])

    return jsonify({'joined_path': joined_path})

if __name__ == '__main__':
    app.run()
