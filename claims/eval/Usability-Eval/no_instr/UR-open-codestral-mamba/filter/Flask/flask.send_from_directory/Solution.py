from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def send_file_route():
    return send_file('/path/to/your/file', attachment_filename='your_filename')

if __name__ == '__main__':
    app.run(debug=True)
