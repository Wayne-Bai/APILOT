import urllib3

def convert_http_response(r):
    http_response = urllib3.response.HTTPResponse()
    http_response.status = r.status
    http_response.reason = r.reason
    http_response.headers = r.getheaders()
    http_response.data = r.read()
    return http_response
