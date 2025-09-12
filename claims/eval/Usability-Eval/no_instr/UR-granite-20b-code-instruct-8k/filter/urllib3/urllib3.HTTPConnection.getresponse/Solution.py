import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://example.com/')
print(r.status)
print(r.data.decode('utf-8'))
