from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def join_paths():
    base_dir = '/path/to/base'
    components = request.args.getlist('path')
    # Safely join the components to the base directory
    joined_path = base_dir
    for component in components:
        joined_path = os.path.join(joined_path, component)

    # Add boundary checks if needed
    if joined_path.startswith(base_dir):
        return f'Successfully joined paths: {joined_path}'
    else:
        return 'Error: resulting path is not safe to use', 400

if __name__ == '__main__':
    app.run(debug=True)
