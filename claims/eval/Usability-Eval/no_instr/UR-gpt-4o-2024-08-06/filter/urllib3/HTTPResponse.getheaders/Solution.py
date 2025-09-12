import urllib3

def get_http_headers(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Getting a view of headers
    headers = response.headers

    # Returning as an unmodifiable data by converting to a frozenset of tuples
    headers_view = frozenset(headers.items())
    
    # Clean up
    response.release_conn()

    return headers_view

# Example usage
url = 'http://example.com'
headers = get_http_headers(url)
print(headers)
