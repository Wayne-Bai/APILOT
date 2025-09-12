from werkzeug.local import LocalProxy
from werkzeug.wrappers import Request

def get_query_string():
    # Returns the `QUERY_STRING` from the WSGI environment.
    request = LocalProxy(lambda: Request._get_current_object())
    return request.environ.get('QUERY_STRING')

# Usage example:
from werkzeug.test import create_environ
from werkzeug.test import run_wsgi_app

app = create_environ(query_string='a=1&b=2')

@app
def application(environ, start_response):
    print(get_query_string())  # prints 'a=1&b=2'
    return []

run_wsgi_app(app, create_environ())
