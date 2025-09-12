import urllib3

# Create an HTTPS connection with the lowest supported version of TLS
http = urllib3.PoolManager(ssl_version=urllib3.util.ssl_.MINIMUM_SUPPORTED)

# Make a request
response = http.request('GET', 'https://example.com')

# Print the response body
print(response.data.decode('utf-8'))
