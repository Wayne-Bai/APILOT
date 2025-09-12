from flask import Flask
app = Flask(__name__)

@app.route("/time")
def time():
    duration = request.args.get('duration')
    if duration is None:
        return "Duration not specified", 400
    try:
        duration = int(duration)
    except ValueError:
        return "Invalid duration specified", 400
    total_seconds = duration * 3600
    return str(total_seconds)

if __name__ == "__main__":
    app.run()
