from flask import Flask, request

app = Flask(__name__)

@app.route('/seconds', methods=['POST'])
def seconds():
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if start_time is None or end_time is None:
        return {'error': 'Start and end time are required'}, 400

    start_time = float(start_time)
    end_time = float(end_time)

    if end_time <= start_time:
        return {'error': 'End time must be greater than start time'}, 400

    total_seconds = (end_time - start_time) / 1000
    return {'total_seconds': total_seconds}

if __name__ == '__main__':
    app.run()
