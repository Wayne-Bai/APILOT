from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/safe_join', methods=['GET'])
def safe_join():
    base_directory = request.args.get('base_directory')
    *untrusted_path_components = request.args.get('path').split('/')

    joined_path = os.path.join(base_directory, *untrusted_path_components)

    return joined_path

if __name__ == '__main__':
    app.run(debug=True)
