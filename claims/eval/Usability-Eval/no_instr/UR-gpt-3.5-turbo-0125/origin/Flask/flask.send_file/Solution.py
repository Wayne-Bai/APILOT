from flask import Flask

app = Flask(__name__)

@app.route('/get_file')
def get_file():
    with open('your_file.txt', 'r') as file:
        file_content = file.read()
    return file_content

if __name__ == '__main__':
    app.run()
