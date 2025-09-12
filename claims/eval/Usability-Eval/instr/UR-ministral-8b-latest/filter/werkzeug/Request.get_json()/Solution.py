from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException
import json

def parse_json_request(data):
    try:
        parsed_data = json.loads(data)
        return Response(parsed_data, mimetype='application/json')
    except json.JSONDecodeError:
        raise HTTPException(description="Invalid JSON", status=400)

# Example usage:
# Assuming incoming JSON request data as a string
request_data = '{"key": "value"}'
response = parse_json_request(request_data)
print(response)
