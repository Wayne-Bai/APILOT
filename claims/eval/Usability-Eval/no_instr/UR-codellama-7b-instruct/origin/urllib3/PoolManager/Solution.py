
import urllib3

# Get a connection from the pool
pool = urllib3.PoolManager()
conn = pool.connection_from_host("example.com")

# Perform an HTTP request with custom cross-host redirect logic and only sends the request-uri portion of the URL
request = conn.request("GET", "/path/to/resource?query=param")

# Check for errors in the response
if request.status == 200:
    # Handle successful request
    pass
else:
    # Handle error response
    print(request.data)
