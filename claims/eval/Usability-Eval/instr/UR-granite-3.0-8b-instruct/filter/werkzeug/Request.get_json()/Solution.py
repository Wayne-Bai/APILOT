from werkzeug.utils import secure_filename
from werkzeug.wrappers import Request

def parse_json_request(request):
    # Create a Request object from the incoming request
    req = Request(request)

    # Parse the JSON data from the request
    data = req.get_json()

    return data
