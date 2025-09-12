import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Define the URL
url = 'http://example.com'

# Make a GET request
response = http.request('GET', url)

# Print the response data
print(response.data)
