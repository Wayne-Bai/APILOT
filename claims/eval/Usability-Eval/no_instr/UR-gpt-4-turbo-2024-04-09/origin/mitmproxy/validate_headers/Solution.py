from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    headers = flow.request.headers
    required_headers = ['Content-Length', 'Transfer-Encoding']

    # Check for conflicting headers that might be exploited in request smuggling
    if 'Content-Length' in headers and 'Transfer-Encoding' in headers:
        raise ValueError("Malformed headers: Both 'Content-Length' and 'Transfer-Encoding' are present.")

    # Additional checks can be done here based on application's needs
    # For instance, checking the validity of 'Transfer-Encoding' header values
    if 'Transfer-Encoding' in headers and headers['Transfer-Encoding'].strip().lower() != 'chunked':
        raise ValueError("Malformed headers: 'Transfer-Encoding' value is not valid or unsupported.")

    # Ensure each header key and value does not contain suspicious characters
    for header_key, header_value in headers.items():
        if '\r' in header_key or '\n' in header_key or '\r' in header_value or '\n' in header_value:
            raise ValueError(f"Malformed headers: Header {header_key} contains invalid characters.")
        
    print("Headers are valid.")
