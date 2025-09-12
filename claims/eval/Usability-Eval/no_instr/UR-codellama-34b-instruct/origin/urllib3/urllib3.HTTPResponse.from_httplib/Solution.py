
import urllib3
from http import HTTPStatus

def convert_http_response(r: HTTPResponse) -> Response:
    """
    Convert an `http.client.HTTPResponse` instance to a `urllib3.response.Response` object.
    """
    response = urllib3.response.Response()
    response.status = r.status
    response.reason = r.reason
    response.headers = dict(r.getheaders())
    if r.chunked():
        response.body = b''.join(iter(r.read, b''))
    else:
        response.body = r.read()
    return response
