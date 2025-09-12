import urllib3

def convert_http_response(r):
    if isinstance(r, http.client.HTTPResponse):
        http_response = urllib3.response.HTTPResponse()
        http_response.__dict__ = r.__dict__
        return http_response
    else:
        raise ValueError("Input is not an http.client.HTTPResponse instance")
