from flask import Flask, send_file

app = Flask(__name__)

@app.route('/send_file')
def send_file_to_client():
    # Replace 'path_to_file' with the actual path to your file
    file_path = 'path_to_file'
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
