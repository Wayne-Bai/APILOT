
from mitmproxy import ctx
from mitmproxy import http

def validate_headers(flow: http.HTTPFlow):
    try:
        if 'host' in flow.request.headers and 'content-length' in flow.request.headers:
            content_length = int(flow.request.headers['content-length'])
            request_body = flow.request.get_content()

            if len(request_body) != content_length:
                raise ValueError('Malformed headers detected!')

    except ValueError as e:
        ctx.log.error(str(e))

def request(flow: http.HTTPFlow):
    validate_headers(flow)

