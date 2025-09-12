from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import BadRequest
import json

@Request.application
def application(request):
    if request.method == 'POST' and request.mimetype == 'application/json':
        data = request.get_json()
        return Response(json.dumps(data), mimetype='application/json')
    else:
        raise BadRequest()

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
