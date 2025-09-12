from flask import Flask, request

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def get_total_seconds():
    duration = request.args.get('duration', default=0, type=int)
    return f"Total seconds covered for {duration} seconds = {duration * 1}"

if __name__ == '__main__':
    app.run()
