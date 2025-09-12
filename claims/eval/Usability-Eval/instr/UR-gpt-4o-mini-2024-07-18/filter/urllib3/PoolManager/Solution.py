import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the target URL and the request-uri portion
base_url = 'http://example.com'
request_uri = '/path/to/resource'

# Make an HTTP request and handle custom cross-host redirects
response = http.request('GET', base_url + request_uri, redirect=True)

# Output the response data
print(response.status)
print(response.data.decode('utf-8'))
