import urllib3

# Create a pool manager
pool_manager = urllib3.PoolManager()

# Make a request to the server
response = pool_manager.request('GET', 'https://example.com')

# Print the response
print(response.data)
