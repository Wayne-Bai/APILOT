from flask import Flask, send_file
 
app = Flask(__name__)
 
@app.route('/send_file')
def send_file():
    return send_file('/path/to/your/file')
 
if __name__ == '__main__':
    app.run()
