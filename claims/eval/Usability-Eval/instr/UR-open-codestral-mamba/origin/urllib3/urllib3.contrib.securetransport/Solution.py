import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.example.com')
print(r.status)
print(r.data)
