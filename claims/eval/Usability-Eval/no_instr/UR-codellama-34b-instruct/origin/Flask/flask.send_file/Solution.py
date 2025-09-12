
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/send-file', methods=['GET'])
def send_file():
    # get the name of the file from the URL parameter
    filename = request.args.get('filename')
    # open the file in binary mode
    with open(filename, 'rb') as f:
        # read the contents of the file
        contents = f.read()
    # send the contents of the file to the client
    return send_file(contents, mimetype='text/plain')
