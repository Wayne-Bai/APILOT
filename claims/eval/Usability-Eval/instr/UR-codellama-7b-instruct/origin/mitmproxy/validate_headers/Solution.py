
from mitmproxy import http

def validate_headers(headers):
    # Check for malformed headers
    if not all(isinstance(value, (bytes, str)) for value in headers.values()):
        raise ValueError("Malformed headers")

    # Check for certain header names
    prohibited_header_names = ["User-Agent", "Cookie"]
    for name in prohibited_header_names:
        if name in headers:
            raise ValueError(f"{name} is a prohibited header")

# Use the validate_headers function to validate the headers of an HTTP request
request = http.HTTPRequest()
request.host = "example.com"
request.port = 80
request.path = "/"
request.method = "GET"
request.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
request.headers["Cookie"] = "test=123"
validate_headers(request.headers)
