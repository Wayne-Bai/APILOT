from flask import Flask, send_file, abort
import os

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    # Define the directory containing the files
    directory = 'path/to/your/directory'

    # Construct the absolute file path
    file_path = os.path.join(directory, filename)

    try:
        # Use send_file to send the file to the client
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        abort(404, description='File not found')

if __name__ == '__main__':
    app.run(debug=True)
