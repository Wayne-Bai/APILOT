import urllib3

# Create an HTTPS connection pool
pool = urllib3.HTTPSConnectionPool(host='www.example.com')

# Send a GET request to the server
response = pool.request('GET', '/')

# Print the response body
print(response.data)
