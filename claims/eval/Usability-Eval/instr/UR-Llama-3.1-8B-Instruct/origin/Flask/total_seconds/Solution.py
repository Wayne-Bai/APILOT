from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Store the total number of seconds in a global variable
total_seconds = 0

# Function to update the total number of seconds
def update_total_seconds(duration):
    global total_seconds
    start_time = total_seconds
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    total_seconds = start_time + (hours * 3600) + (minutes * 60) + seconds

# Route to store duration
@app.route('/duration', methods=['POST'])
def store_duration():
    global total_seconds
    data = request.get_json()
    try:
        duration = float(data['duration'])
        update_total_seconds(duration)
        return jsonify({'message': 'Duration stored successfully', 'total_seconds': total_seconds}), 200
    except ValueError:
        return jsonify({'error': 'Invalid duration'}), 400

# Route to get total seconds
@app.route('/total_seconds', methods=['GET'])
def get_total_seconds():
    global total_seconds
    return jsonify({'total_seconds': total_seconds}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

