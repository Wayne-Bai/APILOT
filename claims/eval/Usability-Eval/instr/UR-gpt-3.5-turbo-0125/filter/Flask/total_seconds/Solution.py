
from flask import Flask
from datetime import datetime

app = Flask(__name__)

def calculate_total_seconds(start_time_str, end_time_str):
    start_time = datetime.fromisoformat(start_time_str)
    end_time = datetime.fromisoformat(end_time_str)
    total_seconds = (end_time - start_time).total_seconds()
    return total_seconds

@app.route('/total_seconds/<start_time_str>/<end_time_str>')
def total_seconds(start_time_str, end_time_str):
    total_seconds = calculate_total_seconds(start_time_str, end_time_str)
    return f'Total seconds: {total_seconds}'

if __name__ == '__main__':
    app.run()
