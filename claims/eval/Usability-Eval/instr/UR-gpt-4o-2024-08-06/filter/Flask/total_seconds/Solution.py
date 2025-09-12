from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/total_seconds', methods=['POST'])
def total_seconds():
    try:
        data = request.get_json()
        start_time_str = data['start_time']
        end_time_str = data['end_time']
        
        # Parse the input time strings into datetime objects
        start_time = datetime.fromisoformat(start_time_str)
        end_time = datetime.fromisoformat(end_time_str)
        
        # Calculate the difference between start and end times
        duration = end_time - start_time
        
        # Get the total seconds from the duration
        total_seconds = duration.total_seconds()
        
        return jsonify({'total_seconds': total_seconds})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
