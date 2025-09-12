import urllib3

http = urllib3.PoolManager()

url = 'http://httpbin.org/redirect-to'
response = http.request('GET', url, headers={'Host': 'httpbin.org'}, fields={'url': 'http://example.com'})
print(response.status)
print(response.data)
