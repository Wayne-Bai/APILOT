import urllib3
from http.client import HTTPResponse

def convert_to_urllib3_response(http_client_response: HTTPResponse) -> urllib3.response.HTTPResponse:
    # Create an instance of urllib3 response
    response = urllib3.response.HTTPResponse(
        body=http_client_response,
        headers=http_client_response.headers,
        status=http_client_response.status,
        reason=http_client_response.reason,
    )
    return response

# Example Usage
# Assume `r` is an instance of http.client.HTTPResponse
# urllib3_response = convert_to_urllib3_response(r)
