from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_time', methods=['POST'])
def calculate_seconds():
    try:
        data = request.get_json()
        hours = data.get('hours')
        minutes = data.get('minutes')
        seconds = data.get('seconds')

        if not all(isinstance(v, (int, float)) and v >= 0 for v in [hours, minutes, seconds]):
            return jsonify({"error": "Invalid input. Hours, minutes, and seconds should be non-negative numbers."}), 400

        total_seconds = hours * 3600 + minutes * 60 + seconds
        return jsonify({"total_seconds": total_seconds})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
