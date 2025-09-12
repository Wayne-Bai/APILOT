import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Make a GET request to the server
response = http.request('GET', 'http://example.com')

# Print the response data
print(response.data.decode('utf-8'))
