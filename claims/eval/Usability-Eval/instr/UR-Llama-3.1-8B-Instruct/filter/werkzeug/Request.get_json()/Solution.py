# Import the necessary modules from Werkzeug
from flask import Flask, request
from flask.json import jsonify

# Create a new instance of the Flask class to create a new WSGI application
app = Flask(__name__)

# Define a new route for your application using the @app.route decorator
@app.route('/parse_json', methods=['POST'])
def parse_json():
    try:
        # Get the JSON data from the request
        json_data = request.get_json()
        
        # Parse the incoming JSON request data
        if json_data is not None:
            return jsonify(json_data)
        else:
            return jsonify({"error": "No JSON data provided"}), 400
    
    except Exception as e:
        return jsonify({"error": "Failed to parse JSON data: " + str(e)}), 500

# Run the application on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
