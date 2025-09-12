import urllib3

# Create a new HTTP connection pool
http = urllib3.PoolManager()

# Define the URL to send the request to
url = "http://example.com"

# Send a GET request to the server
response = http.request('GET', url)

# Print the response status code
print(response.status)

# Print the response data
print(response.data.decode())
