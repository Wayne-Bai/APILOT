from flask import Flask, request

app = Flask(__name__)

@app.route('/seconds', methods=['GET'])
def get_seconds():
    duration_hours = int(request.args.get('hours', 0))
    duration_minutes = int(request.args.get('minutes', 0))
    duration_seconds = int(request.args.get('seconds', 0))

    total_seconds = duration_hours * 3600 + duration_minutes * 60 + duration_seconds

    return {
        'duration_hours': duration_hours,
        'duration_minutes': duration_minutes,
        'duration_seconds': duration_seconds,
        'total_seconds': total_seconds
    }

if __name__ == '__main__':
    app.run(debug=True)
