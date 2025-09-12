import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Open a connection
response = http.request('GET', 'http://httpbin.org/get')

# Get the header values
headers = response.headers

# Print the values of all headers
for k, v in headers.items():
    print(f'{k}: {v}')
