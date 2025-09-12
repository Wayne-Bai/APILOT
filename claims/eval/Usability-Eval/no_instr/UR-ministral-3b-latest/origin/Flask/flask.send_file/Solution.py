from flask import Flask, send_file
app = Flask(__name__)

@app.route('/file', methods=['GET'])
def serve_file():
    return send_file('path_to_your_file.txt')

if __name__ == '__main__':
    app.run()
