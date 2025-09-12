from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/join_path', methods=['GET'])
def join_path():
    base_dir = request.args.get('base_dir')
    components = request.args.getlist('components')

    # Use os.path.join to safely join the base directory and components
    joined_path = os.path.join(base_dir, *components)

    return joined_path

if __name__ == '__main__':
    app.run(debug=True)
