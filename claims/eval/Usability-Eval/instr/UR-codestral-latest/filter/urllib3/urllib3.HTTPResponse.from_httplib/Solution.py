import urllib3
from urllib3.response import HTTPResponse
import http.client

def create_urllib3_response(http_response: http.client.HTTPResponse) -> HTTPResponse:
    http_version = http_response.version
    status = http_response.status
    reason = http_response.reason
    headers = http.client.HTTPMessage(http_response.headers)

    # convert the headers to a format that urllib3.response.HTTPResponse accepts
    headers_dict = {k: v for k, v in headers.items()}

    # create a new urllib3.response.HTTPResponse instance
    urllib3_response = HTTPResponse(
        body=http_response.read(),
        headers=headers_dict,
        status=status,
        reason=reason,
        preload_content=False,
        original_response=http_response
    )

    urllib3_response._fp = urllib3.response.HTTPResponse._original_response(urllib3_response.body)
    urllib3_response._fp.version = http_version
    urllib3_response._fp.status = status
    urllib3_response._fp.reason = reason

    return urllib3_response
