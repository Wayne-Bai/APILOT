import urllib3
from urllib3.response import HTTPResponse

class CustomHTTPResponse(HTTPResponse):
    def __init__(self, http_response):
        super().__init__(
            headers=http_response.headers.items(),
            status=http_response.status,
            data=http_response.read(),
            version=None,  # HTTP version
            url=http_response.headers['URL'] if 'URL' in http_response.headers else '',
            reason=http_response.reason
        )

def http_response_to_urllib3(response):
    return CustomHTTPResponse(response)

# Usage
if __name__ == "__main__":
    # Example usage with an HTTPResponse
    import http.client

    http_response = http.client.HTTPResponse(
        status=200,
        version=8,
        reason="OK",
        headers=[('Server', 'gw'),
                 ('Date', 'Fri, 10 Mar 2023 10:29:28 GMT'),
                 ('Content-Type', 'text/html; charset=UTF-8'),
                 ('Content-Length', '221')],
        message=b"- stag\n"
    )
    urllib3_response = http_response_to_urllib3(http_response)
    print(urllib3_response.data.decode())
