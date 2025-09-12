from flask import Flask
app = Flask(__name__)

@app.route('/seconds/<int:hours>/<int:minutes>/<int:seconds>')
def total_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return f"Total seconds: {total_seconds}"

if __name__ == '__main__':
    app.run()
