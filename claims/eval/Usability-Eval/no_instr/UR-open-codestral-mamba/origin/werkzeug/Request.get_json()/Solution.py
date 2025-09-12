Python
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import BadRequest
import json

@Request.application
def application(request):
    if request.method == 'POST':
        try:
            data = request.get_json()
            return Response(json.dumps(data), mimetype='application/json', status=200)
        except BadRequest as e:
            return Response("Invalid request: {0}".format(e), status=400)
    else:
        return Response(status=405)
