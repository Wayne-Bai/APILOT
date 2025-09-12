from flask import Flask, request

app = Flask(__name__)

@app.route('/seconds', methods=['POST'])
def get_seconds():
    data = request.get_json()
    duration = data.get('duration', 0)
    return {'total_seconds': duration}

if __name__ == '__main__':
    app.run(debug=True)
