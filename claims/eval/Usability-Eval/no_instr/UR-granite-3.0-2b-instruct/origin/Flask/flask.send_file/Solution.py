from flask import Flask, send_file

app = Flask(__name__)

@app.route('/file')
def file():
    with open('path/to/your/file.txt', 'rb') as f:
        return send_file(f, as_attachment=True)

if __name__ == '__main__':
    app.run()
