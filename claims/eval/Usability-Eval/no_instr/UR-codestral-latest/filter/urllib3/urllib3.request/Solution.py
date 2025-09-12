import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Make a GET request
response = http.request('GET', 'http://example.com')

# Print the response data
print(response.data)
