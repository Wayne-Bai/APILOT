
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')

# Specify the number of bytes to read from the response body
amt = 100

# Read and return the response body, or up to the next 'amt' bytes
body = response.read(amt)

print(body)
