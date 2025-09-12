from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/path', methods=['POST'])
def join_path():
    json_data = request.get_json()
    if not json_data or 'base_dir' not in json_data or 'path_components' not in json_data:
        abort(400, 'Invalid request data. Must include base_dir and path_components.')

    base_dir = json_data['base_dir']
    path_components = json_data['path_components']

    import os

    # Safely join the path components
    safe_path = os.path.join(base_dir, *path_components)

    if not os.path.isdir(safe_path):
        return {'error': 'Invalid path components could not form a valid directory.'}, 400

    return {'safe_path': safe_path}, 200

if __name__ == '__main__':
    app.run(debug=True)
