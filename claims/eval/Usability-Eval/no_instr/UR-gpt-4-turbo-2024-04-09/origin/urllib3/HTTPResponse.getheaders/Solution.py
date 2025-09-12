import urllib3
from types import MappingProxyType

def fetch_headers(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    headers = response.headers
    # Creating an unmodifiable view of the headers
    unmodifiable_headers = MappingProxyType(headers)
    return unmodifiable_headers

# Usage example
url = 'http://example.com'
headers = fetch_headers(url)
print(headers)
