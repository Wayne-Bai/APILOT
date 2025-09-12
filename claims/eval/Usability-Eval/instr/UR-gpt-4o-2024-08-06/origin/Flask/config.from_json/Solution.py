from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_mapping(
    DEBUG=True,
    SECRET_KEY='default_key',
    USERNAME='admin',
    PASSWORD='password'
)

@app.route('/update-config', methods=['POST'])
def update_config():
    if request.is_json:
        config_updates = request.get_json()
        if isinstance(config_updates, dict):
            app.config.from_mapping(config_updates)
            return jsonify({"message": "Configurations updated successfully", "new_config": config_updates}), 200
        else:
            return jsonify({"error": "Invalid JSON format"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
