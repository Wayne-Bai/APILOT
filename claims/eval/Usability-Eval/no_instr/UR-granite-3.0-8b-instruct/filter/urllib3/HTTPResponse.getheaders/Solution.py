import urllib3

def get_headers(response):
    return response.headers

# Example usage:
http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')
headers = get_headers(response)
print(headers)
