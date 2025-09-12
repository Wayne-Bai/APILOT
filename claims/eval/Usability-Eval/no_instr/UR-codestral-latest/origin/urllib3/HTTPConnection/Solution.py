import urllib3

# Create a connection pool
http = urllib3.PoolManager()

# Define the URL
url = 'http://www.example.com'

# Define a timeout (in seconds)
timeout = 10

# Define a source address (optional)
# source_address = ('local_host', 1234)

# Define a blocksize for sending a file-like message body (optional)
# blocksize = 8192

# Make a request
r = http.request('GET', url, timeout=timeout)

# Print the response
print(r.status)
print(r.data)
