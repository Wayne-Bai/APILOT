from flask import Flask, send_file

app = Flask(__name__)

@app.route('/get-file')
def get_file():
    file_path = 'path_to_your_file.txt'  # Specify the correct path to your file
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)
