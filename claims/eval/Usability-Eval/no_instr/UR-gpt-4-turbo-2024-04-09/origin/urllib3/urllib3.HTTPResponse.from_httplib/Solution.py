import urllib3
from http.client import HTTPResponse

def convert_to_urllib3_response(r):
    # Create an HTTPResponse object for urllib3 from the http.client.HTTPResponse
    if not isinstance(r, HTTPResponse):
        raise TypeError("Expected http.client.HTTPResponse instance")

    # Initialize HTTPResponse for urllib3 using information from http.client.HTTPResponse
    urllib3_response = urllib3.response.HTTPResponse(
        body=r.read(),
        status=r.status,
        headers=r.headers,
        reason=r.reason,
        preload_content=False
    )
    
    return urllib3_response
