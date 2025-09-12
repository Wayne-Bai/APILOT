import urllib3

# Create a custom context for the HTTP connection
http = urllib3.PoolManager(
    context={'ssl_version': urllib3.util.sslparse.get_protocol_version('TLSv1.2')})

# Use the custom context to make a request
response = http.request('GET', 'https://example.com')

# Print the response
print(response.data)
