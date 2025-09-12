from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    headers = flow.request.headers

    # Validate the headers for content-length and transfer-encoding inconsistencies
    if 'Content-Length' in headers and 'Transfer-Encoding' in headers:
        raise ValueError("Malformed Header: Both 'Content-Length' and 'Transfer-Encoding' headers are present.")
    
    # Additional checks for irregular use of Transfer-Encoding values
    if 'Transfer-Encoding' in headers:
        te_values = headers['Transfer-Encoding'].split(',')
        if 'chunked' not in te_values or te_values[-1].strip() != 'chunked':
            raise ValueError("Malformed Header: Invalid 'Transfer-Encoding' values. 'Chunked' must be the last value if present.")

    # Check for unusual Content-Length values or multiple instances which might be used to obscure the header
    if headers.get_all('Content-Length'):
        if len(headers.get_all('Content-Length')) > 1:
            raise ValueError("Malformed Header: Multiple 'Content-Length' headers are present.")
        try:
            lengths = [int(cl) for cl in headers.get_all('Content-Length')]
            if lengths.count(lengths[0]) != len(lengths):
                raise ValueError("Malformed Header: Inconsistent 'Content-Length' values provided.")
        except ValueError:
            raise ValueError("Malformed Header: Non-integer 'Content-Length' value detected.")
