import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the base URL and the request URI
base_url = 'http://example.com'
request_uri = '/path/to/resource'

# Perform the request, specifying the full URL and enabling redirect
response = http.request('GET', base_url + request_uri, redirect=True)

# Print response data
print("Status:", response.status)
print("Response data:", response.data.decode('utf-8'))

# Release the connection back to the pool
response.release_conn()
