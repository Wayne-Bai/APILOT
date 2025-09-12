import urllib3

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Make a request to a URL
response = http.request('GET', 'http://example.com')

# Get the headers from the response
headers = response.headers

# Print the headers and corresponding values
for header, value in headers.items():
    print(f"{header}: {value}")
