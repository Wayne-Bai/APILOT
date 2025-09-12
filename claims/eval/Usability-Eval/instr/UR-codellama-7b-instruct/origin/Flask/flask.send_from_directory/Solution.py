import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/send-file', methods=['GET'])
def send_file():
    # get the file path from the request query parameter
    file_path = request.args.get('file_path')

    # check if the file exists
    if not os.path.isfile(file_path):
        abort(404)

    # read the file's contents
    with open(file_path, 'r') as f:
        data = f.read()

    # return the file's contents as a response
    return data

if __name__ == '__main__':
    app.run(debug=True)