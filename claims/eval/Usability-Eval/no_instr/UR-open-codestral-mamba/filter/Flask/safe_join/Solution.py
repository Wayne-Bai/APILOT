from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/join_paths', methods=['GET'])
def join_paths():
    base_dir = '/path/to/base/directory'  # replace with your base directory
    user_input = request.args.get('user_input', '')  # get the user input from the request

    # safely join the base directory with the user input
    safe_path = os.path.join(base_dir, user_input)

    return safe_path

if __name__ == '__main__':
    app.run(debug=True)
