from werkzeug.exceptions import BadRequest
from werkzeug.wrappers import Request, Response
import json

def handle_request(environ, start_response):
    request = Request(environ)
    
    try:
        # Get JSON data from the request
        json_data = request.get_json()
        if json_data is None:
            raise BadRequest("Invalid JSON data")
        
        # Create a response
        response_data = {
            "success": True,
            "data": json_data
        }
        
        response = Response(json.dumps(response_data), content_type='application/json', status=200)
    except BadRequest as e:
        response = Response(json.dumps({"success": False, "error": str(e)}), content_type='application/json', status=400)
    
    return response(environ, start_response)
