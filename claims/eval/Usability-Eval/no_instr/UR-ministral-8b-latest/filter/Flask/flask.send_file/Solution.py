from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/send-file', methods=['GET', 'POST'])
def send_file():
    if request.method == 'POST':
        file_path = request.files['file'].filename
        # Assuming the file is saved within the application directory
        # You can change the directory path according to your file structure
        return send_from_directory('/path/to/your/files', file_path)
    elif request.method == 'GET':
        # Provide response for GET request if necessary
        pass
    return "Provide a valid request."

if __name__ == '__main__':
    app.run(debug=True)
