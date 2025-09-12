
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://httpbin.org/headers')
headers = response.headers

# Creating a read-only view of the headers
unmodifiable_headers = http.HTTPHeaderDict(headers)

print(unmodifiable_headers)
