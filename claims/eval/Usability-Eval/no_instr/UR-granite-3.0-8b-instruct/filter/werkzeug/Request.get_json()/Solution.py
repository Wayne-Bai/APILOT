from werkzeug.utils import secure_filename
import json

def parse_json_request():
    # Assuming the JSON data is sent in the request body
    json_data = request.get_json()
    return json_data
