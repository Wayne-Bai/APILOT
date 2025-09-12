from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        # Adjust the directory path as needed
        directory = 'your_directory_path'  # Replace with your directory path
        return send_file(f'{directory}/{filename}', as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
