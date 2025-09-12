
from werkzeug.wrappers import Request

def get_query_string(environ):
    request = Request(environ)
    return request.query_string

# Example usage
query_string = get_query_string(my_wsgi_environment)
print(query_string)
