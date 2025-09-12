from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/total_seconds', methods=['POST'])
def get_total_seconds():
    """
    Calculate the total number of seconds for a given time duration.
    
    Request body should be in the following format:
    {
        "minutes": int,
        "seconds": int
    }
    
    Response:
    {
        "total_seconds": int
    }
    """
    
    # Get the request body
    data = request.get_json()
    
    # Check if required fields are present
    if'minutes' not in data or'seconds' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Extract minutes and seconds from the request body
    minutes = data['minutes']
    seconds = data['seconds']
    
    # Validate if minutes and seconds are integers
    if not isinstance(minutes, int) or not isinstance(seconds, int):
        return jsonify({"error": "Minutes and seconds should be integers"}), 400
    
    # Validate if minutes and seconds are non-negative
    if minutes < 0 or seconds < 0:
        return jsonify({"error": "Minutes and seconds should be non-negative"}), 400
    
    # Calculate the total seconds
    total_seconds = minutes * 60 + seconds
    
    # Return the result as JSON
    return jsonify({"total_seconds": total_seconds}), 200

if __name__ == '__main__':
    app.run(debug=True)
