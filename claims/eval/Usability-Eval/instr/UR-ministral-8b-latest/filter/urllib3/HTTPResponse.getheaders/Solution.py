import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Create a request to a URL
response = http.request('GET', 'https://httpbin.org/headers')

# Get the headers of the response
headers = response.headers

# Print the headers as a dictionary
print(dict(headers))
