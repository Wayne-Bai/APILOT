import urllib3

def convert_http_client_response_to_urllib3(r):
    # Create a urllib3.response.HTTPResponse object
    urllib3_response = urllib3.response.HTTPResponse(
        body=r.read(),
        headers=r.headers,
        status=r.status,
        version=r.version,
        reason=r.reason,
        preload_content=False
    )
    
    return urllib3_response
