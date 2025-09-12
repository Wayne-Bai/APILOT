
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if not flow.request.headers or not flow.response.headers:
        raise ValueError("Request or response headers are missing.")
    
    for key in flow.request.headers.keys():
        if not isinstance(flow.request.headers[key], str):
            raise ValueError(f"Malformed request header: {key}")

    for key in flow.response.headers.keys():
        if not isinstance(flow.response.headers[key], str):
            raise ValueError(f"Malformed response header: {key}")
