import urllib3

def convert_http_response(r):
    """
    Convert an http.client.HTTPResponse instance r to a corresponding
    urllib3.response.HTTPResponse object.
    """
    urllib3_response = urllib3.response.HTTPResponse()
    urllib3_response.status = r.status
    urllib3_response.reason = r.reason
    urllib3_response.version = r.version
    urllib3_response.headers = r.getheaders()
    urllib3_response.data = r.read()

    return urllib3_response
