# Importing the required libraries
from flask import Flask, send_file
import os

# Creating a Flask application object
app = Flask(__name__)

# Routing to send a file from a directory
@app.route('/send_file', methods=['GET'])
def send_file_route():
    # Specifying the path to the file you want to send
    file_path = os.path.join(os.getcwd(), 'example.txt')  # Replace 'example.txt' with your file name and path

    # Checking if the file exists
    if os.path.isfile(file_path):
        # Sending the file to the client
        return send_file(file_path, as_attachment=True, attachment_filename='example.txt')
    else:
        return 'File not found', 404

# Running the application on local host and port 5000
if __name__ == '__main__':
    app.run(debug=True)
