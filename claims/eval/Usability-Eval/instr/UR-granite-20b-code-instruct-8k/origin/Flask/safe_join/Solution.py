from flask import Flask, safe_join
app = Flask(__name__)

@app.route("/")
def index():
    base_dir = "/tmp"
    untrusted_paths = ["foo", "bar"] # Replace with your untrusted path components
    safe_paths = safe_join(base_dir, *untrusted_paths)
    return safe_paths

if __name__ == "__main__":
    app.run()
