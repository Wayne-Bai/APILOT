import urllib3

# Create a HTTP pool object for the hostname and port
pool = urllib3.HTTPConnectionPool('www.example.com')

# Make a GET request to the server
response = pool.request('GET', '/path/to/resource')

# Get the response body as a string
body = response.read()
