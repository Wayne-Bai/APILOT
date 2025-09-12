import urllib3

url = 'http://example.com/path'
method = 'GET'
# Alternatively you can instantiate this once for all your requests
http = urllib3.PoolManager()
response = http.request(method, url)

# Use the response object as normal...
print(response.data)
