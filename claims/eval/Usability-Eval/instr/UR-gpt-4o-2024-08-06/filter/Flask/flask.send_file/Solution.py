from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    # Define the directory where files are stored
    file_directory = 'files'

    # Check if the file exists in the directory
    if os.path.exists(os.path.join(file_directory, filename)):
        # Send the file to the client
        return send_from_directory(directory=file_directory, filename=filename, as_attachment=True)
    else:
        # If the file is not found, return a 404 error
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
