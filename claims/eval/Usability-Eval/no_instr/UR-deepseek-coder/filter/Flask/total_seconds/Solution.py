from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/seconds', methods=['GET'])
def get_seconds():
    # Get the duration in hours, minutes, and seconds from the query parameters
    hours = int(request.args.get('hours', 0))
    minutes = int(request.args.get('minutes', 0))
    seconds = int(request.args.get('seconds', 0))
    
    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # Return the result as a JSON response
    return jsonify({'total_seconds': total_seconds})

if __name__ == '__main__':
    app.run(debug=True)
