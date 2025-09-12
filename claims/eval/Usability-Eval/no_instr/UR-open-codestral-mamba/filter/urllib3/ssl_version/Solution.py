import urllib3

# Create a connection pool
http = urllib3.PoolManager()

# Define the URL of the server that you want to connect to
url = 'https://example.com'

# Make a GET request to the server
response = http.request('GET', url)

# Extract the SSL version being used
ssl_version = response.version

print('Supported SSL versions at the server configuration:', ssl_version)
