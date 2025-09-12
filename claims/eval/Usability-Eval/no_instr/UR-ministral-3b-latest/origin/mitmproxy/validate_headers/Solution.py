from mitmproxy import http

def validate_request_headers(flow: http.HTTPFlow) -> None:
    custom_headers = ['Content-Length', 'X-Requested-With']
    for header in flow.request.headers:
        if header.key not in custom_headers:
            raise ValueError(f"Malformed header: {header.key}")

    flow.response.headers.add('Set-Cookie', 'customHeader=value')
