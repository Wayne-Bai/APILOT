from flask import Flask

app = Flask(__name__)

# Helper function for safe joining
def safe_join(base, *paths):
    import os
    joined_path = os.path.join(base, *paths)
    return joined_path

@app.route('/safe_join')
def safe_join_route():
    base = "/some/base/path"
    paths = ["safe", "relative", "path", "components"]
    safe_joint_path = safe_join(base, *paths)
    return f'Joined path: {safe_joint_path}'

if __name__ == '__main__':
    app.run(debug=True)
