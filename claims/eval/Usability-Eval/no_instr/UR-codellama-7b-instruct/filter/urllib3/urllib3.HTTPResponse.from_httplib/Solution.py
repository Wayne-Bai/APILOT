
import urllib3

def create_urllib3_response(r: http.client.HTTPResponse) -> urllib3.response.HTTPResponse:
    # Create a new URLlib3 response object from the given HTTP response
    return urllib3.response.HTTPResponse(
        body=r.read(),
        headers={name: value for name, value in r.getheaders()},
        status=r.status,
        version=r.version,
    )
