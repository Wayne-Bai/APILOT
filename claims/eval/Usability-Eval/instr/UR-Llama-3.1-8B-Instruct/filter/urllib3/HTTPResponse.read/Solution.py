import urllib3

# Set up HTTP client
http = urllib3.PoolManager()

# Example URL and amount of bytes to read
url = 'http://httpbin.org/blocking/1'
amt = 10  # bytes

# Send an HTTP GET request
response = http.request('GET', url)

# Read and print the response body, or up to amt bytes
print(response.data[:amt])
