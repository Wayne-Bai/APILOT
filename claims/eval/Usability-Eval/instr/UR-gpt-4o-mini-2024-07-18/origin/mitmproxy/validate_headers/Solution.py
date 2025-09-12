from mitmproxy import http

def validate_headers(flow: http.HTTPFlow) -> None:
    """
    Validate HTTP headers to prevent request smuggling attacks.
    Raises a ValueError if headers are malformed.
    """
    # Define a list of headers that are required
    required_headers = ['Host', 'Content-Length']

    # Check for missing required headers
    for header in required_headers:
        if header not in flow.request.headers:
            raise ValueError(f"Missing required header: {header}")

    # Example of additional validation checks
    # Check for Content-Length to be a valid integer
    if 'Content-Length' in flow.request.headers:
        try:
            content_length = int(flow.request.headers['Content-Length'])
            if content_length < 0:
                raise ValueError("Content-Length must be a non-negative integer.")
        except ValueError:
            raise ValueError("Content-Length is malformed. It must be an integer.")

    # You can add more validation rules as needed
