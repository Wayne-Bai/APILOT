from werkzeug.wrappers import Request

def application(environ, start_response):
    request = Request(environ)
    query_string = request.query_string
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [query_string]
