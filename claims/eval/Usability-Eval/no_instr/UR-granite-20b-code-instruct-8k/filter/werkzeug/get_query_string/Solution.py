from werkzeug.wrappers import Request
from werkzeug.routing import Rule
from werkzeug.wsgi import SharedDataMiddleware

@Request.application
def application(request):
    return f"The QUERY_STRING is: {request.args}"

if __name__ == "__main__":
    application.run()
