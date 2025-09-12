
from flask import Flask

app = Flask(__name__)

def calculate_seconds(duration):
    start_time, end_time = duration.split('-')
    start_hour, start_minute, start_second = map(int, start_time.split(':'))
    end_hour, end_minute, end_second = map(int, end_time.split(':'))
    
    total_seconds = (end_hour - start_hour) * 3600 + (end_minute - start_minute) * 60 + (end_second - start_second)
    
    return total_seconds

@app.route('/calculate_total_seconds/<string:duration>')
def calculate_total_seconds(duration):
    total_seconds = calculate_seconds(duration)
    return f'Total number of seconds covered for the specified duration is: {total_seconds}'

if __name__ == '__main__':
    app.run()
