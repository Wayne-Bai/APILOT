from werkzeug import Request, parse_json

def parse_json_request(request):
    """
    Parses the incoming JSON request data and returns it.

    :param request: The request object containing the JSON data.
    :return: The parsed JSON data as a Python dictionary.
    """
    json_data = parse_json(request.get_data())
    return json_data
