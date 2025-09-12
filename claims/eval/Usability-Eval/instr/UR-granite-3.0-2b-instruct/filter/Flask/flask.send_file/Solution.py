from flask import Flask, send_file

app = Flask(__name__)

@app.route('/file')
def file_transfer():
    return send_file('path_to_your_file.txt', as_attachment=True)

if __name__ == '__main__':
    app.run()
