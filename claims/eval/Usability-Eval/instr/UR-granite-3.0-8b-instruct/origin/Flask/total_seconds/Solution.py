from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def total_seconds():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    if not start_time or not end_time:
        return "Both start_time and end_time are required.", 400

    try:
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD HH:MM:SS.", 400

    total_seconds = (end_time - start_time).total_seconds()
    return f"The total number of seconds covered is: {total_seconds}"

if __name__ == '__main__':
    app.run(debug=True)
