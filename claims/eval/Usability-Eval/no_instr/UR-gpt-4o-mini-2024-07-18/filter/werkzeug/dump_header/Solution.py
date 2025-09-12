from werkzeug.wrappers import Request, Response

def dump_http_header(environ):
    request = Request(environ)
    headers = request.headers
    header_info = {key: value for key, value in headers.items()}
    
    return header_info

def application(environ, start_response):
    headers = dump_http_header(environ)
    response = Response(str(headers), content_type='application/json')
    return response(environ, start_response)
