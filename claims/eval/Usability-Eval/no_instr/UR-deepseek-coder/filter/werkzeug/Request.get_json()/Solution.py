from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import json

@Request.application
def application(request):
    if request.method == 'POST':
        data = request.get_json()
        return Response(json.dumps(data), mimetype='application/json')
    return Response('Only POST requests are supported', status=405)

if __name__ == '__main__':
    run_simple('localhost', 5000, application)
