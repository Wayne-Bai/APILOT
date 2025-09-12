import urllib3

def fetch_url(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response

# Example usage
url = "http://example.com"
response = fetch_url(url)
print(response.status)
print(response.data)
