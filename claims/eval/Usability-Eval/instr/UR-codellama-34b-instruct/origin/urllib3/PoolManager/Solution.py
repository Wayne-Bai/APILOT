
import urllib3

# Create a pool manager
pool_manager = urllib3.PoolManager()

# Get a connection from the pool
connection = pool_manager.connection_from_url('https://www.example.com')

# Set up the HTTP request with custom cross-host redirect logic
redirect_headers = {'Host': 'www.example.com'}
response = connection.request(
    'GET',
    '/path/to/resource',
    headers=redirect_headers,
    allow_redirects=True,
)

# Print the response status code and headers
print(response.status)
print(response.headers)
