import urllib3

# Create a pool manager to manage the connections
http = urllib3.PoolManager()

# Define the request method and URI
method = 'GET'
url = 'http://example.com/path'

# Send the request
response = http.request(method, url)

# Print the response status code and data
print('Status Code:', response.status)
print('Data:', response.data.decode('utf-8'))
