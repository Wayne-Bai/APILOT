from werkzeug.wrappers import Request

def get_query_string(environ):
    request = Request(environ)
    return request.query_string
