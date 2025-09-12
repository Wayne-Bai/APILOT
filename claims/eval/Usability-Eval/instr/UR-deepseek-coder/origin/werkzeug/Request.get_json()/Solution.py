from werkzeug.wrappers import Request, Response
import json

@Request.application
def application(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        data = json.loads(request.data)
        return Response(json.dumps(data), content_type='application/json')
    return Response('Invalid request', status=400)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application)
