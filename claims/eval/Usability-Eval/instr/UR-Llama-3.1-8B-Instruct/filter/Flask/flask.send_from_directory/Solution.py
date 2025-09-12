# Import required libraries
from flask import Flask, send_file
import os
from werkzeug.utils import secure_filename

# Create a new instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/', methods=['GET'])
def home():
    # Specify the path to the file you want to send
    upload_folder = 'files'
    
    # Create a directory if it does not exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Get the filename
    filename = 'example.txt'

    # Check if the file exists, take care of the filename and send the safe filename
    if os.path.exists(os.path.join(upload_folder, filename)):
        return send_file(os.path.join(upload_folder, filename), as_attachment=True)
    else:
        return "File does not exist"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
