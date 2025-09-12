from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Define the expected headers and their required formats
    expected_headers = {
        "Content-Length": r"^\d+$",  # Content-Length should be a positive integer
        "Transfer-Encoding": r"^chunked$",  # Transfer-Encoding should be 'chunked'
        "Connection": r"^close|keep-alive$"  # Connection should be 'close' or 'keep-alive'
    }

    # Check each expected header
    for header, pattern in expected_headers.items():
        if header in flow.request.headers:
            value = flow.request.headers[header]
            if not re.match(pattern, value):
                raise ValueError(f"Malformed header '{header}': '{value}' does not match expected pattern '{pattern}'")
        else:
            raise ValueError(f"Missing required header: '{header}'")
