
from werkzeug.wrappers import Request
from werkzeug.datastructures import ImmutableMultiDict
import json

def parse_json_request(request):
    # Parse the JSON request data using Request and json libraries
    parsed_data = Request(request).get_json()
    return parsed_data
