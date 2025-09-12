import urllib3

def convert_http_response(r):
    return urllib3.response.HTTPResponse.from_httplib(r)
