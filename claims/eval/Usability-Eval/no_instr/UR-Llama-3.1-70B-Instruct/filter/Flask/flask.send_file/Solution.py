from flask import Flask, send_file

app = Flask(__name__)

# Define the route to send the file
@app.route('/download-file')
def download_file():
    # Specify the path to the file
    file_path = 'example.txt'
    
    # Send the file to the client
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
