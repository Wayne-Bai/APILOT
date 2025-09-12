from flask import Flask, send_file

# Create Flask application
app = Flask(__name__)

# Define the path to the directory containing the files
FILE_DIRECTORY = '/path/to/your/directory'

# Define a route to download a file
@app.route('/download/<filename>')
def download_file(filename):
    """
    Send a file from within a directory using send_file().

    :param filename: The name of the file to be sent.
    :return: The file as a response.
    """
    try:
        # Check if the file exists in the directory
        file_path = f'{FILE_DIRECTORY}/{filename}'
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        # Return a 404 error if the file does not exist
        return 'File not found', 404

if __name__ == '__main__':
    app.run(debug=True)
