from werkzeug import Request, utils
import json

def parse_json_request(request: Request):
    json_data = request.get_data()
    if json_data:
        try:
            data = json.loads(json_data)
            return utils.jsonify(data)
        except json.JSONDecodeError:
            return "Invalid JSON data", 400
    else:
        return "No JSON data found", 400
