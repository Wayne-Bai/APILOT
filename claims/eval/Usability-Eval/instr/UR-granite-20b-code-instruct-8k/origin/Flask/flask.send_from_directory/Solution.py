from flask import Flask, send_file

app = Flask(__name__)

@app.route("/send_file")
def send_file_example():
    file_path = "/path/to/file.txt"  # Replace with the actual file path
    return send_file(file_path)

if __name__ == "__main__":
    app.run()
