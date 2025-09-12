
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/duration_to_seconds", methods=["POST"])
def duration_to_seconds():
    # Get the duration from the request body
    duration = request.get_json()["duration"]
    
    # Convert the duration to a timedelta object
    td = datetime.timedelta(days=duration)
    
    # Calculate the total number of seconds covered
    total_seconds = td.total_seconds()
    
    return {"total_seconds": total_seconds}
