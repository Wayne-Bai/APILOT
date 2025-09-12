import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')
print(response.data)
