from flask import Flask, safe_join
app = Flask(__name__)

@app.route('/')
def index():
    base_dir = '/path/to/base/directory'
    untrusted_paths = ['path1', 'path2', 'path3']
    safe_paths = safe_join(base_dir, *untrusted_paths)
    return f"Safe paths: {safe_paths}"

if __name__ == '__main__':
    app.run()
