
from datetime import timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/duration', methods=['GET'])
def get_duration():
    # Parse the duration from the request parameters
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    duration = timedelta(start_time, end_time)
    
    # Calculate the total number of seconds covered by the duration
    total_seconds = duration.total_seconds()
    
    return jsonify({'total_seconds': total_seconds})
