
import urllib3

# Create a connection pool manager
pool = urllib3.PoolManager()

# Get a connection from the pool
conn = pool.connection_from_url('https://www.example.com')

# Perform an HTTP request with custom cross-host redirect logic and only sends the request-uri portion of the URL
response = conn.request(
    method='GET',
    url=urllib3.make_headers(default_port=443, headers={'Host': 'www.example.com'}),
    headers={'Connection': 'keep-alive'},
)

# Print the response status code and message
print('Response Status Code:', response.status)
print('Response Message:', response.reason)
