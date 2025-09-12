from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/getfile/<filename>')
def get_file(filename):
    return send_file(os.path.join('path_to_your_directory', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
