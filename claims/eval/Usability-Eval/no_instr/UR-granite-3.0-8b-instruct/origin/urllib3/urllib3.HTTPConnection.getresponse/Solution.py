import urllib3

# Create a custom HTTP connection pool
http = urllib3.PoolManager()

# Define the URL
url = "http://example.com"

# Send a GET request to the server
response = http.request('GET', url)

# Print the response status code and data
print(f"Status code: {response.status}")
print(f"Response data: {response.data.decode('utf-8')}")
