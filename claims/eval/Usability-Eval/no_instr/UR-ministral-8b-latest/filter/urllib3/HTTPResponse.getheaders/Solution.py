import urllib3
from collections.abc import Mapping

http = urllib3.PoolManager()

def fetch_headers(url):
    response = http.request('GET', url)
    return _unmodifiable_headers(response.headers)

def _unmodifiable_headers(headers):
    return frozenset([(name, value) for name, value in headers.items()])

# Example usage:
url = 'https://httpbin.org/headers'
headers = fetch_headers(url)
print(headers)
