from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    headers = flow.request.headers
    
    # Check for the presence of required headers
    required_headers = ["Content-Length", "Transfer-Encoding"]
    for header in required_headers:
        if header not in headers:
            raise ValueError(f"Missing required header: {header}")
    
    # Check for malformed headers
    if "chunked" in headers.get("Transfer-Encoding", "").lower():
        if "Content-Length" in headers:
            raise ValueError("Malformed headers: Content-Length should not be present when Transfer-Encoding is chunked")
    
    # Additional checks can be added here as needed
