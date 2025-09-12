import urllib3

def get_headers(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return {key: value for key, value in response.headers}

# Example usage
url = 'https://example.com'
headers = get_headers(url)
print(headers)
