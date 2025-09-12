from flask import Flask, request

app = Flask(__name__)

@app.route('/seconds', methods=['GET'])
def get_seconds():
    time_str = request.args.get('time', default = "00:00:00", type = str)
    h, m, s = map(int, time_str.split(':'))
    return str(h * 3600 + m * 60 + s)

if __name__ == '__main__':
    app.run(debug=True)
