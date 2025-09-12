from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/total_seconds', methods=['POST'])
def total_seconds():
    data = request.get_json()
    start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    total_seconds = (end_time - start_time).total_seconds()
    return {'total_seconds': total_seconds}

if __name__ == '__main__':
    app.run(debug=True)
