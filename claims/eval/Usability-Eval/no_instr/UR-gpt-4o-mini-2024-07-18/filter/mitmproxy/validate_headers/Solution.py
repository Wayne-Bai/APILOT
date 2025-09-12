from mitmproxy import http

def validate_headers(flow: http.HTTPFlow) -> None:
    """
    Validate HTTP headers to avoid request smuggling attacks.

    Raises a ValueError if headers are malformed.
    """
    headers = flow.request.headers

    # Example validation logic
    if 'Content-Length' in headers:
        try:
            content_length = int(headers['Content-Length'])
            if content_length < 0:
                raise ValueError("Content-Length must be a non-negative integer.")
        except ValueError:
            raise ValueError("Content-Length header is malformed.")

    if 'Transfer-Encoding' in headers and headers['Transfer-Encoding'].lower() == 'chunked':
        raise ValueError("Chuncked Transfer-Encoding is not allowed.")

# Add this function to the mitmproxy event hooks
from mitmproxy import ctx

def response(flow: http.HTTPFlow) -> None:
    try:
        validate_headers(flow)
    except ValueError as e:
        ctx.log.error(f"Header validation error: {e}")
        flow.response = http.Response.make(
            400,  # HTTP status code
            b"Bad Request: " + str(e).encode()  # HTTP response body
        )
