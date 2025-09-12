from werkzeug.wrappers import Response

def dump_http_header(header):
    response = Response()
    response.headers[header] = 'example_value'
    return response.headers[header]
