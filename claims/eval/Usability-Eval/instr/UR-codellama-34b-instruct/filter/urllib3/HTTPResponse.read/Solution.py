import urllib3

# Create a connection pool manager object
http = urllib3.PoolManager()

# Perform a GET request on the given URL
response = http.request('GET', 'https://www.example.com')

# Get the response body
body = response.data

# Print the first 1024 bytes of the response body
print(body[:1024])
