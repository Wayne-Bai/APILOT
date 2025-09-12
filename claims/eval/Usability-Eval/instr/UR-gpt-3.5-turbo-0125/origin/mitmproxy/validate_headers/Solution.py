
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    headers = flow.request.headers
    # Check for Content-Length header
    if 'Content-Length' in headers:
        content_length = headers['Content-Length']
        if not content_length.isdigit():
            raise ValueError("Malformed Content-Length header detected")

    # Check for Transfer-Encoding header
    if 'Transfer-Encoding' in headers:
        transfer_encoding = headers['Transfer-Encoding']
        if not transfer_encoding.lower() == 'chunked':
            raise ValueError("Malformed Transfer-Encoding header detected")

    # Check for other potential headers that may be used in request smuggling attacks

    # Note: Add more header checks as needed to secure against request smuggling attacks
