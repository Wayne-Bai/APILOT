from flask import Flask, send_file

app = Flask(__name__)

@app.route('/send_file/<filename>')
def send_file_route(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
