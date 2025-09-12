import urllib3
from urllib.parse import urlparse

class NoRedirectPoolManager(urllib3.PoolManager):
    def _should_redirect(self, method, scheme, response, redirect_location):
        return False

def make_http_request(url):
    parsed_url = urlparse(url)
    request_uri = f'{parsed_url.path}?{parsed_url.query}' if parsed_url.query else parsed_url.path

    http = NoRedirectPoolManager()
    conn = http.connection_from_url(url)

    conn.request("GET", request_uri)
    response = conn.getresponse()
    data = response.read()

    return data

# Usage
url = "http://example.com/some/path?param=value"
print(make_http_request(url))
