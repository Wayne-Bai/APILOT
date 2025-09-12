from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/sendfile/<path:filename>')
def sendfile(filename):
    return send_from_directory(app.root_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
