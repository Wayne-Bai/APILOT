from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/update_config", methods=["POST"])
def update_config():
    data = request.get_json()
    for key, value in data.items():
        app.config[key] = value
    return jsonify({"message": "Config updated successfully."})
