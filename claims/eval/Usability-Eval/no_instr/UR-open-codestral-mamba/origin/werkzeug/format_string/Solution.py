from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

@Request.application
def application(request):
    return Response('Hello, %s!' % request.args.get('name', 'World'))

if __name__ == '__main__':
    run_simple('localhost', 4000, application)
