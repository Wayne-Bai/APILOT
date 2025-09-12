import urllib3

def url_response_transfer(http_response: http.client.HTTPResponse) -> urllib3.response.HTTPResponse:
    url = http_response.geturl()
    return urllib3.response.HTTPResponse(
        url,
        status=http_response.status,
        headers={'USER-AGENT': 'libcurl'},
        method='GET',
    )

# Example usage:
# http_resp = http.client.HTTPResponse(urlopen("http://example.com"))
# print(url_response_transfer(http_resp))
