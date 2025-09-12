from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    query_string = request.query_string.decode('utf-8')

    response = Response(query_string)
    return response(environ, start_response)
