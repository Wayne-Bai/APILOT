
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    total_seconds = (datetime.datetime.strptime(end_time, "%H:%M:%S") - datetime.datetime.strptime(start_time, "%H:%M:%S")).total_seconds()
    return f"Total number of seconds covered: {total_seconds}"
