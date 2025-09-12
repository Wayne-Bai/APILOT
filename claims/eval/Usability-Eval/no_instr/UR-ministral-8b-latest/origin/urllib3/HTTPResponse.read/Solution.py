import urllib3

# Create an HTTP request
http = urllib3.PoolManager()
url = 'http://example.com'
response = http.request('GET', url)

# Extract the response body or up to the next amount of bytes
response_body = response.data.decode('utf-8')[:1000]  # reads up to 1000 bytes

print(response_body)
