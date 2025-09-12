from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/seconds', methods=['POST'])
def count_seconds():
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if start_time and end_time:
        seconds = (end_time - start_time) / 1000
        return jsonify({'seconds': int(seconds)})
    else:
        return jsonify({'error': 'Both start_time and end_time are required'}), 400

if __name__ == '__main__':
    app.run()
