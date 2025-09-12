
from flask import Flask, safe_join

app = Flask(__name__)

@app.route('/')
def index():
    base_dir = "/path/to/base/directory"
    trusted_path = "trusted_folder"
    untrusted_path = "../../../untrusted_folder"

    joined_path = "/".join([base_dir, trusted_path, untrusted_path.split("/")[0]])

    return f"Safely joined path: {joined_path}"

if __name__ == '__main__':
    app.run()
