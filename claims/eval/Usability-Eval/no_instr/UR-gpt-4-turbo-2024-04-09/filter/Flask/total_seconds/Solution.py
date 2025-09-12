from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def total_seconds():
    hours = request.args.get('hours', default=0, type=int)
    minutes = request.args.get('minutes', default=0, type=int)
    seconds = request.args.get('seconds', default=0, type=int)

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return jsonify({"total_seconds": total_seconds})

if __name__ == '__main__':
    app.run(debug=True)
