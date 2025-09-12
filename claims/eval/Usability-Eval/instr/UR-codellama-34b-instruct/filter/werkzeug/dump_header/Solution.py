from werkzeug import *

# Create a simple Werkzeug application
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the request headers
    headers = request.headers

    # Print the headers
    for key, value in headers:
        print(key, value)

if __name__ == '__main__':
    app.run()
