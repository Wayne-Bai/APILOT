
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/duration/seconds', methods=['POST'])
def calculate_seconds():
    data = request.json
    duration = data.get('duration')

    if not duration:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        time_parts = duration.split(':')
        if len(time_parts)!= 3:
            return jsonify({'error': 'Invalid duration format. Use HH:MM:SS'}), 400

        hours, minutes, seconds = map(int, time_parts)
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return jsonify({'total_seconds': total_seconds}), 200
    except ValueError:
        return jsonify({'error': 'Invalid duration format. Use HH:MM:SS'}), 400

if __name__ == '__main__':
    app.run(debug=True)
