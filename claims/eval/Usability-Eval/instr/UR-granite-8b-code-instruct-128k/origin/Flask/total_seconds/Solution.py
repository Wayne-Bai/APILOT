import flask
from datetime import datetime

app = flask.Flask(__name__)

@app.route("/duration")
def duration():
    start_time = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime("2023-01-02 13:00:00", "%Y-%m-%d %H:%M:%S")
    duration_seconds = (end_time - start_time).total_seconds()
    return str(duration_seconds)

if __name__ == "__main__":
    app.run()
