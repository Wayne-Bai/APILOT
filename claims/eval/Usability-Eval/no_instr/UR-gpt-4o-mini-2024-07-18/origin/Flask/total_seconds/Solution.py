from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def total_seconds():
    duration = request.args.get('duration', default='0:0:0', type=str)
    
    try:
        hours, minutes, seconds = map(int, duration.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return jsonify({'total_seconds': total_seconds}), 200
    except ValueError:
        return jsonify({'error': 'Invalid duration format. Use HH:MM:SS.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
