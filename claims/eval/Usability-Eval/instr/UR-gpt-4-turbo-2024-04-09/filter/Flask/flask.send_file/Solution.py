from flask import Flask, send_file

app = Flask(__name__)

@app.route('/send-file')
def send_file_route():
    # Specify the path to your file
    file_path = 'path/to/your/file.ext'
    # Ensure the file exists and is accessible
    try:
        return send_file(file_path)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
