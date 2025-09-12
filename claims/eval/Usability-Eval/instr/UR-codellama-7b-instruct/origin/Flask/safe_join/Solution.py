
from flask import Flask, safe_join

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def user(username):
    username = username.strip()
    if username != '' and not '/' in username:
        return render_template('profile.html', username=username)
    else:
        abort(404)
