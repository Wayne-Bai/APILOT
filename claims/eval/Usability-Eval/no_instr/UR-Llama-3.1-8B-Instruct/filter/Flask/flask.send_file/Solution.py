# Import the Flask framework
from flask import Flask, send_file, send_from_directory
import os

# Create a new instance of the Flask application
app = Flask(__name__)

# Set the path of the file that you want to send to the client
# Replace 'path_to_your_file' with the actual path to your file
file_path = 'path_to_your_file.txt'

# Define a route for handling GET requests
@app.route('/file', methods=['GET'])
def send_file_to_client():
    """
    Send the contents of a file to the client.
    
    Returns:
        A response object containing the file contents.
    """
    try:
        # Check if the file exists
        if os.path.isfile(file_path):
            # Send the file contents to the client
            with open(file_path, 'r') as file:
                file_contents = file.read()
                return {'file_contents': file_contents}
        else:
            # Return an error message if the file does not exist
            return {'error': 'File not found'}, 404
    except Exception as e:
        # Return an error message if an exception occurs
        return {'error': str(e)}, 500

# Run the application on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
