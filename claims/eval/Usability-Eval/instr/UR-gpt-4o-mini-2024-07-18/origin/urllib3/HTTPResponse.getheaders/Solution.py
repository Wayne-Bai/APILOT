import urllib3

class HTTPHeadersView:
    def __init__(self, headers):
        self._headers = headers

    def items(self):
        return self._headers.items()

    def keys(self):
        return self._headers.keys()

    def values(self):
        return self._headers.values()

# Example usage
http = urllib3.PoolManager()
response = http.request('GET', 'https://httpbin.org/get')

headers_view = HTTPHeadersView(response.headers)
print("Headers:", headers_view.items())
print("Keys:", headers_view.keys())
print("Values:", headers_view.values())
