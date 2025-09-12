import urllib3

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Specify the URL you want to request
url = 'http://example.com'

# Make a GET request to the server
response = http.request('GET', url)

# Print the response data
print(response.data.decode('utf-8'))

# Optional: check the response status
print("Response status:", response.status)
