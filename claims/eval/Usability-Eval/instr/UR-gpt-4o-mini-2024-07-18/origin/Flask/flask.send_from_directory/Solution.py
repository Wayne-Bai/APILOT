from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    # Specify the directory where the files are located
    directory = 'your_directory'  # Change this to your directory path
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
