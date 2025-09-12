from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def time_difference():
    start_time_str = request.args.get('start_time')
    end_time_str = request.args.get('end_time')

    try:
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid date format, please use YYYY-MM-DD HH:MM:SS'}), 400

    duration = end_time - start_time
    total_seconds = int(duration.total_seconds())

    return jsonify({'total_seconds': total_seconds})

if __name__ == '__main__':
    app.run(debug=True)
