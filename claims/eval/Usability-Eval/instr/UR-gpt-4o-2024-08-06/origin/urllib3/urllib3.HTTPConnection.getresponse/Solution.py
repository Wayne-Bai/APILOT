import urllib3

# Create a PoolManager instance to handle HTTP requests
http = urllib3.PoolManager()

# Define the URL to send the request to
url = 'http://example.com'

# Send a GET request to the server
response = http.request('GET', url)

# Print the response received from the server
print(response.data.decode('utf-8'))
