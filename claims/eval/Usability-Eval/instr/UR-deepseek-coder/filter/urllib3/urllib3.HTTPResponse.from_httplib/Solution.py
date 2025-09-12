import urllib3

def convert_to_urllib3_response(http_client_response):
    # Create a urllib3.response.HTTPResponse object
    urllib3_response = urllib3.response.HTTPResponse(
        body=http_client_response.read(),
        headers=http_client_response.headers,
        status=http_client_response.status,
        version=http_client_response.version,
        reason=http_client_response.reason,
        preload_content=False
    )
    return urllib3_response
