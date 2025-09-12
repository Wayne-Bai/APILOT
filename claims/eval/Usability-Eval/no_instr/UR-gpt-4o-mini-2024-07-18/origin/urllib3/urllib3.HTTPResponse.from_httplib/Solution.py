import urllib3
from urllib3.response import HTTPResponse

def convert_http_response(r):
    # Create a new instance of a urllib3 response using the body and headers from the HTTPResponse instance
    return HTTPResponse(
        body=r.read(),
        headers=r.getheaders(),
        preload_content=False,
        strict=False
    )
