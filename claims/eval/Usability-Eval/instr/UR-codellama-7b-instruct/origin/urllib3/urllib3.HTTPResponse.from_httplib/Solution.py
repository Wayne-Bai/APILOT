
import urllib3

def response_from_http(r: http.client.HTTPResponse) -> urllib3.response.HTTPResponse:
    # Create a new urllib3.response.HTTPResponse object from the given HTTPResponse instance
    return urllib3.response.HTTPResponse(r.fp, r._method, r.url, r.headers, r.version, r.chunked)
