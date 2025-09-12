import urllib3
from urllib3.response import HTTPResponse

def convert_response(r):
    """
    Convert http.client.HTTPResponse instance to urllib3.response.HTTPResponse object.

    :param r: Instance of http.client.HTTPResponse
    :return: Instance of urllib3.response.HTTPResponse
    """
    # Extract headers from the http.client.HTTPResponse
    headers = {k: v for k, v in r.getheaders()}
    
    # Create a new urllib3 HTTPResponse object
    urllib3_response = HTTPResponse(
        body=r.read(),  # Read the body data from the original response
        headers=headers,  # Use the headers from the original response
        status=r.status,  # Use the status from the original response
        reason=r.reason,  # Use the reason from the original response
        preload_content=False  # Avoid pre-loading content
    )
    
    return urllib3_response
