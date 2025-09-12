from werkzeug import Request, public

def unquote_header(header):
    request = Request(environ={})
    header_value = request.headers.get(header)
    if header_value:
        return unquote(header_value)
    else:
        return None
