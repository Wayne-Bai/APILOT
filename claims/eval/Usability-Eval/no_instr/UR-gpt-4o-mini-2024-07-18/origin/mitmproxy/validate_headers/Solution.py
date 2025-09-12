from mitmproxy import http

def validate_headers(flow: http.HTTPFlow) -> None:
    headers = flow.request.headers

    # Check for common header formats that might lead to request smuggling
    if 'Content-Length' in headers and 'Transfer-Encoding' in headers:
        raise ValueError("Both 'Content-Length' and 'Transfer-Encoding' headers are present.")

    if 'Transfer-Encoding' in headers and headers['Transfer-Encoding'].lower() != 'chunked':
        raise ValueError("Invalid 'Transfer-Encoding' value.")

    if 'Content-Length' in headers:
        try:
            content_length = int(headers['Content-Length'])
            if content_length < 0:
                raise ValueError("Content-Length must be a non-negative integer.")
        except ValueError:
            raise ValueError("Content-Length header is malformed.")

def request(flow: http.HTTPFlow) -> None:
    try:
        validate_headers(flow)
    except ValueError as e:
        flow.response = http.HTTPResponse.make(
            400,  # Bad Request
            f"Header validation error: {str(e)}",
            {"Content-Type": "text/plain"}
        )
