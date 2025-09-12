from flask import Flask, send_file, request, abort

app = Flask(__name__)

@app.route('/send-file', methods=['GET'])
def send_file_to_client():
    # Define the path to the file you want to send
    file_path = 'path_to_your_file.txt'  # Update this with the actual file path

    try:
        # Send the file to the client
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        abort(404, description="File not found.")

if __name__ == '__main__':
    app.run(debug=True)
