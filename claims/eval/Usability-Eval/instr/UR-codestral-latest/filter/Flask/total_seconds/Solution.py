from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/seconds', methods=['POST'])
def seconds():
    data = request.get_json()
    hours = data.get('hours', 0)
    minutes = data.get('minutes', 0)
    seconds = data.get('seconds', 0)

    total_seconds = seconds + minutes * 60 + hours * 3600

    return jsonify({"total_seconds": total_seconds}), 200

if __name__ == '__main__':
    app.run(debug=True)
