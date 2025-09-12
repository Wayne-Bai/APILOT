import urllib3

# Create a HTTPS connection pool with hostname verification
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='path/to/your/ca_certs.pem',  # Replace with the path to your CA certificates file
    maxsize=10,  # Maximum number of connections in the pool
    block=True,  # Block until a connection is available
)

# Make a request with hostname verification
response = http.request('GET', 'https://example.com')

# Print the response status code
print(response.status)
