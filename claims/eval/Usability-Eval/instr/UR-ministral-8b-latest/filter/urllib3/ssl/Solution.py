import urllib3

# Create a pool manager
pool_manager = urllib3.PoolManager()

# Encrypt HTTPS request
response = pool_manager.request('GET', 'https://example.com')

# Print the status code and body of the response
print(response.status)
print(response.data.decode('utf-8'))
