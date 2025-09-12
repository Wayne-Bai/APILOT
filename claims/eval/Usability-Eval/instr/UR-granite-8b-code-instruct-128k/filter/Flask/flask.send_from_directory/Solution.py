from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/send_file')
def send_file_route():
    # specify the directory and file name
    file_path = '/path/to/your/directory/your_file.txt'
    # check if the file exists
    if os.path.isfile(file_path):
        # send the file
        return send_file(file_path)
    else:
        # handle the case when the file does not exist
        return 'File not found'

if __name__ == '__main__':
    app.run()
