import urllib3

# Create a pool manager instance for sending requests.
http = urllib3.PoolManager()

# Specify the URL
url = "http://example.com"

# Send a GET request to the server
response = http.request('GET', url)

# Print the response data
print(response.data)
