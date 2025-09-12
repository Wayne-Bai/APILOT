import urllib3

http = urllib3.PoolManager()
url = 'http://your-absolute-path.com'
method = 'GET'  # or 'POST', 'PUT', 'DELETE', etc.

response = http.request(method, url)

# To check the response data:
print(response.data)
