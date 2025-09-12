# Importing the Flask class from the flask module
from flask import Flask, send_file

# Create a new instance of the Flask class
app = Flask(__name__)

# Define a route for handling GET requests to the /file endpoint
@app.route('/file', methods=['GET'])
def get_file():
    # Replace 'path_to_your_file.txt' with the actual path to your file
    file_path = 'path_to_your_file.txt'

    # Check if the file exists
    if not file_path.split('/')[-1].endswith('.txt'):
        return {'error': 'Only.txt files are supported'}, 400
    if not file_path.endswith('.txt'):
        return {'error': 'Only.txt files are supported'}, 400

    # Send the file back to the client using the send_file function
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return {'error': 'Failed to send file'}, 500

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
