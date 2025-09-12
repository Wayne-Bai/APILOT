from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound

@Request.application
def application(request):
    headers = request.headers
    return Response(str(headers), mimetype='text/plain')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, application)
