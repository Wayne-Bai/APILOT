from flask import Flask

app = Flask(__name__)
app.config.from_json('config.json')

@app.route('/update-config', methods=['GET'])
def update_config():
    app.config.from_json('config.json', force=True)
    return "Config updated successfully"

if __name__ == '__main__':
    app.run(debug=True)
