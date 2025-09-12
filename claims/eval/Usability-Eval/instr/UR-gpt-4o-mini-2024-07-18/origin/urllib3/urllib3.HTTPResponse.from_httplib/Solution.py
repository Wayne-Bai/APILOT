import urllib3
from http.client import HTTPResponse as HttpClientResponse

def convert_http_client_response_to_urllib3_response(http_client_response: HttpClientResponse) -> urllib3.response.HTTPResponse:
    # Create a memory file-like object from the original HTTPResponse
    from io import BytesIO
    body = BytesIO(http_client_response.read())
    
    # Get the status and headers from the original response
    status = http_client_response.status
    headers = dict(http_client_response.getheaders())
    
    # Create a new urllib3 response object
    return urllib3.response.HTTPResponse(
        body=body,
        status=status,
        headers=headers,
        preload_content=True
    )
