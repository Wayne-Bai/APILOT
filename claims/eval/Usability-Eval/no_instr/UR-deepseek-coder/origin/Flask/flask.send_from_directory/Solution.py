from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = f"path/to/your/directory/{filename}"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
