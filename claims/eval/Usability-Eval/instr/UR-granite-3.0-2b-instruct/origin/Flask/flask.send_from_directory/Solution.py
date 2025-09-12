from flask import Flask, send_file

app = Flask(__name__)

@app.route('/file/<path:filename>')
def send_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
