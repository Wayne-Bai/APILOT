from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/duration', methods=['POST'])
def calculate_duration():
    data = request.json
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    
    if not start_time or not end_time:
        return jsonify({"error": "Please provide both start_time and end_time"}), 400

    try:
        # Parse the start and end times
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
        
        # Calculate the duration
        duration = end - start
        
        # Get total seconds
        total_seconds = int(duration.total_seconds())
        
        return jsonify({"total_seconds": total_seconds})
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400

if __name__ == '__main__':
    app.run(debug=True)
