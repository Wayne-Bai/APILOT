
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def calculate_total_seconds():
    data = request.get_json()
    start_time = data["start_time"]
    end_time = data["end_time"]
    total_seconds = (end_time - start_time).total_seconds()
    return str(total_seconds)

if __name__ == "__main__":
    app.run(debug=True)
