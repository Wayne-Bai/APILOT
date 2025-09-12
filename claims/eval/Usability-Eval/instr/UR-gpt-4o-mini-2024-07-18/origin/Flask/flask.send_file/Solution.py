from flask import Flask, Response

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return Response(open(filename, 'rb'), mimetype='application/octet-stream', headers={"Content-Disposition": f"attachment;filename={filename}"})
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
