from flask import Flask
import os

app = Flask(__name__)

@app.route('/secure-path/<path:subpath>')
def secure_path(subpath):
    base_directory = '/safe/base/directory'
    secure_full_path = os.path.join(base_directory, *subpath.split('/'))
    return f"The secure path is: {secure_full_path}"

if __name__ == "__main__":
    app.run(debug=True)
