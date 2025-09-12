import urllib3

# Create a pool manager with SSL verification and hostname checking enabled
pool = urllib3.HTTPSConnectionPool(
    'example.com',
    port=443,
    cert_reqs='CERT_REQUIRED',
    ssl_version=urllib3.PROTOCOL_TLS_CLIENT,
)

# Make a request to the server
response = pool.request('GET', '/')

# Print the response status and body
print(response.status)
print(response.data)
