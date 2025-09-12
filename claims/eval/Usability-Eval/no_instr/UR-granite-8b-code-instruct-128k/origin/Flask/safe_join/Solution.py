from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/safe-join/<path:base_directory>/<path:untrusted_path>')
def safe_join(base_directory, untrusted_path):
    return os.path.join(base_directory, *untrusted_path.split('/'))

if __name__ == '__main__':
    app.run()
