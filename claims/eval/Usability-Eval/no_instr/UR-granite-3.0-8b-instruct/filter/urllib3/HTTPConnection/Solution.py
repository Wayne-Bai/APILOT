import urllib3

# Create an HTTP connection instance
http_conn = urllib3.PoolManager()

# Make a GET request
response = http_conn.request('GET', 'http://example.com')

# Print the response status code
print(response.status)

# If the response is a file-like object, you can read its content
if hasattr(response, 'data'):
    print(response.data.decode())
