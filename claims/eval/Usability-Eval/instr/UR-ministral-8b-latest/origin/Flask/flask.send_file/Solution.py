from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download/<path:filepath>')
def download_file(filepath):
    try:
        return send_file(filepath, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
