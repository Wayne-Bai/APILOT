from werkzeug.wrappers import Request, Response

def dump_http_headers(environ):
    request = Request(environ)
    headers = request.headers

    header_info = {key: value for key, value in headers.items()}
    return header_info

def application(environ, start_response):
    headers = dump_http_headers(environ)
    response_body = str(headers).encode('utf-8')
    response = Response(response_body, content_type='application/json')
    
    return response(environ, start_response)
