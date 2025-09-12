from flask import Flask, request, jsonify
from datetime import timedelta

app = Flask(__name__)

@app.route('/total_seconds')
def get_total_seconds():
    time_str = request.args.get('duration', '00:00:00')
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        total_seconds = int(duration.total_seconds())
        return jsonify({'total_seconds': total_seconds})
    except ValueError:
        return jsonify({'error': 'Invalid time format. Please use HH:MM:SS format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
