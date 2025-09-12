
from werkzeug.wrappers import Request

def get_query_string(environ):
    request = Request(environ)
    return request.query_string

# Example usage:
environ = {
    'QUERY_STRING': 'key1=value1&key2=value2'
}
print(get_query_string(environ))
