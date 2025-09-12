
from werkzeug.wrappers import Request
from werkzeug.datastructures import MultiDict

def parse_json(request):
    if not hasattr(request, 'data'):
        return None
    try:
        data = json.loads(request.data)
    except ValueError as e:
        raise BadRequest('Invalid JSON request') from e
    return MultiDict(data)
