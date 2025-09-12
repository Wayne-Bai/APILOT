from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/send-file", methods=["GET"])
def send_file():
    # Define the path to the file you want to send
    filepath = "path/to/your/file"

    # Open the file in binary mode
    with open(filepath, "rb") as f:
        # Read the file contents into a bytes object
        data = f.read()

    # Set the appropriate headers for your file
    headers = {
        "Content-Type": "application/octet-stream",
        "Content-Disposition": f"attachment; filename={os.path.basename(filepath)}"
    }

    # Return the file contents with the appropriate headers
    return data, 200, headers
