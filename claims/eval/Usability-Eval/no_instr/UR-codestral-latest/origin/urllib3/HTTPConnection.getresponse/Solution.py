import urllib3

# Create a PoolManager instance for sending requests
http = urllib3.PoolManager()

# Send a GET request to the server
# Replace 'http://server.com' with the actual server URL
response = http.request('GET', 'http://server.com')

# Print the HTTP status code
print('HTTP Status Code:', response.status)

# Print the response data
print('Response Data:', response.data)
