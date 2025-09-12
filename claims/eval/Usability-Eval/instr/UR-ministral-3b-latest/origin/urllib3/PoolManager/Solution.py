import urllib3

# Initializing the HTTP Pool Manager
http = urllib3.PoolManager()

# Set up the connection details
url = 'http://example.com/path/to/resource'
redirects = 5

# Generate the connection and perform the HTTP request
response = http.request(
    method='GET',
    url=url,
    redirects=redirects,
    prepare_headers={'Host': 'example.com'},
    headers={'User-Agent': 'example_ua'}
)

# Print the status code and response data
print(f'Status Code: {response.status}')
print(f'Response Data: {response.data.decode("utf-8")}')
