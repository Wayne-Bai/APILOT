from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound, MethodNotAllowed
from json import dumps

# Create a URL routing map to handle the JSON requests
url_map = Map([
    Rule('/handle_json', endpoint='handle_json')
])

@Request.application
def application(request):
    adapter = url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return getattr(request, endpoint)(request, **values)
    except NotFound:
        return Response('Not Found', status=404)
    except MethodNotAllowed:
        return Response('Method Not Allowed', status=405)

def handle_json(request):
    if request.method == 'POST':
        data = request.get_json()
        return Response(dumps(data), mimetype='application/json')
