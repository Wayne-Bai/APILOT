import urllib3

# Initialize the urllib3 pool manager
http = urllib3.PoolManager()

# Define the pool key
pool_key = 'http://example.com'

# Setup a connection pool based on the provided pool key
# Note that when using PoolManager, it will automatically create a ConnectionPool for each host you request
connection_pool = http.connection_from_url(pool_key)

# Use the connection_pool to make a request (example)
response = connection_pool.request('GET', '/')

# Print the response status and data
print(f'Status: {response.status}')
print(f'Data: {response.data.decode("utf-8")}')
