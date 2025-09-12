import urllib3

# Create a PoolManager, which is an object that handles details of connection pooling and thread safety
http = urllib3.PoolManager()

# Define the URL you want to send the request to
url = "http://example.com"

# Send a GET request to the server
response = http.request('GET', url)

# Print the response data
print(response.data)
