
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'Hello, {}! You are {} years old.'.format(name, age)

if __name__ == '__main__':
    app.run(debug=True)
