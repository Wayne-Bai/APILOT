import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com', redirect=False)
print(response.data)
