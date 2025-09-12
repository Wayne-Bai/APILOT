from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/total_seconds/<string:duration>', methods=['GET'])
def get_total_seconds(duration):
    """Returns the total number of seconds covered for the specified duration."""
    
    seconds_per_unit = {
       's': 1,
       'm': 60,
        'h': 3600,
        'd': 86400
    }
    
    unit = duration[-1]
    value = int(duration[:-1])
    
    if unit in seconds_per_unit:
        total_seconds = value * seconds_per_unit[unit]
        return {"total_seconds": total_seconds}
    else:
        return {"error": "Invalid unit. Supported units are's' for seconds,'m' for minutes, 'h' for hours, 'd' for days."}, 400

if __name__ == '__main__':
    app.run(debug=True)
