from flask import Flask, make_response, send_from_directory
import os

app = Flask(__name__)

@app.route('/get_file/<filename>')
def send_file(filename):
    directory = 'path/to/your/directory'
    response = make_response(send_from_directory(directory, filename))
    response.headers["Content-Disposition"] = "attachment; filename=" + filename
    return response

if __name__ == '__main__':
    app.run(debug=True)
