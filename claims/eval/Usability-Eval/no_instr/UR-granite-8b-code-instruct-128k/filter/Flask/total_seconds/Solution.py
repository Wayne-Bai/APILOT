from flask import Flask, request

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def total_seconds():
    duration = request.args.get('duration')
    total_seconds = int(duration.total_seconds())
    return str(total_seconds)

if __name__ == '__main__':
    app.run()
