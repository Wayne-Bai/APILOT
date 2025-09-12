from flask import Flask, url_for

app = Flask(__name__)

# Base directory
base_dir = "/var/www/html"

# Function to safely join untrusted path components
def join_path(base, *paths):
    for path in paths:
        if not path.startswith('./') and not path.startswith('../'):
            path = '/' + path
        if path.startswith('/'):
            return '/' + path
    return base

@app.route('/(join_path_example)')
def join_path_example():
    base = join_path(base_dir, 'foo')
    return f"Safely joined path: {url_for('static', filename=base + 'bar.html')}"

@app.route('/relative_path_example')
def relative_path_example():
    relative_path = join_path(base_dir)
    return f"No leading slash added: {url_for('static', filename=relative_path + 'bar.html')}"

if __name__ == '__main__':
    app.run(debug=True)
