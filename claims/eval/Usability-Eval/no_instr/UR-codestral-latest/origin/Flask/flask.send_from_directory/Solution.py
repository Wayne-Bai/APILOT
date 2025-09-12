from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/sendfile/<filename>')
def send_file(filename):
    directory = 'uploads'
    try:
        return send_from_directory(directory, filename)
    except:
        return "File not found", 404

if __name__ == '__main__':
    app.run()
