import urllib3

# Create a pool of connections
http = urllib3.PoolManager()

# Define the hostname and URL
hostname = 'example.com'
url = 'http://{}/api/data'.format(hostname if hostname else '127.0.0.1')

# Build the request
response = http.request('GET', url)

# Print and process the response
print(response.status)
print(response.data)
