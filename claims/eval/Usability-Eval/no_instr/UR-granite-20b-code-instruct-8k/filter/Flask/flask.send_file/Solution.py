from flask import Flask, send_file

app = Flask(__name__)

@app.route('/send_file')
def send_file_to_client():
    file_path = 'path_to_your_file'
    return send_file(file_path)

if __name__ == '__main__':
    app.run()
