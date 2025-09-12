from flask import Flask, send_file

app = Flask(__name__)

@app.route('/sendfile')
def send_file_example():
    file_path = 'path/to/your/file.txt'  # replace with your file path
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
