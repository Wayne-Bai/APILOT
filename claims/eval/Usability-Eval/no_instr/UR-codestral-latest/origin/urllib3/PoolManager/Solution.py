import urllib3
from urllib.parse import urlsplit

def send_request(url):
    # Creates a pool manager instance for sending requests
    http = urllib3.PoolManager()

    # Splits the URL into components
    url_parts = urlsplit(url)

    # Prepare the URL for the request
    request_url = url_parts.path
    if url_parts.query:
        request_url += '?' + url_parts.query

    # Send HTTP request
    res = http.request('GET', url, url=request_url)

    return res.status, res.data

# Example usage
status, data = send_request('http://example.com/path?query=value')
print(status)
print(data)
