from flask import Flask
import time

app = Flask(__name__)

@app.route('/getseconds/<int:duration>')
def get_seconds(duration):
    current_time = time.time()
    time_to_add = current_time + duration
    while time.time() < time_to_add:
        pass
    time_difference = time.time() - current_time
    return str(time_difference)

if __name__ == '__main__':
    app.run(debug=True)
