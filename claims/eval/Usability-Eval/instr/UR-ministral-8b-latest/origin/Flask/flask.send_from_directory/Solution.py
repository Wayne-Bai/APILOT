from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/send-file/<filename>')
def send(file_name):
    try:
        file_path = os.path.join(app.root_path, 'uploads', file_name)
        if os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "File not found", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
