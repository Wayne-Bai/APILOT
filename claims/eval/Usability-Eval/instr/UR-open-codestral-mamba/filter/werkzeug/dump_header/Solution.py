# Importing required module from werkzeug
from werkzeug.wrappers import Request

# Dump an HTTP header again
@Request.application
def application(request):
    headers = request.headers  # Get the headers from the request
    return '\n'.join(['{}: {}'.format(k, v) for k, v in headers])  # Return the headers

# running the application
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application)
