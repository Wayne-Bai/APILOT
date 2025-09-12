# Importing the required modules
from flask import Flask, send_file

# Creating a Flask application
app = Flask(__name__)

# Defining a route to send a file
@app.route('/download_file/<string:filename>')
def download_file(filename):
    # Specify the directory path where the file is located
    directory_path = 'your_directory_path'

    # Try to send the file
    try:
        return send_file(directory_path + '/' + filename, as_attachment=True)

    # Handle the case when the file does not exist
    except FileNotFoundError:
        return f"The file {filename} does not exist in the directory."

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
