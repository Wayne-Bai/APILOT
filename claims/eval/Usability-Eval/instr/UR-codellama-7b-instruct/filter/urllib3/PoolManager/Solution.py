
import urllib3

# Get a connection from the pool
conn = urllib3.connection_from_url('http://www.example.com')

# Perform an HTTP request with custom cross-host redirect logic
request = conn.request('GET', '/path/to/resource', redirect=True, redirect_args={'method': 'GET'})

# Only sends the request-uri portion of the URL
response = request.get_response()

print(response.status)
