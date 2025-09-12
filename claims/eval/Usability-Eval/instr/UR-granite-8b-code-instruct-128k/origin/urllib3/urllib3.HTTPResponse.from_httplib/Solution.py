import urllib3

def generate_urllib3_response(http_client_response):
    """
    Generate a urllib3.response.HTTPResponse object from an http.client.HTTPResponse instance.
    """
    urllib3_response = urllib3.response.HTTPResponse(body=http_client_response.read())
    urllib3_response.begin()
    return urllib3_response
