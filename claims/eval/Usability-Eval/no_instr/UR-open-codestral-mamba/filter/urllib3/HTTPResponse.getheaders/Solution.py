import urllib3

http = urllib3.PoolManager()
headers = http.request('GET', 'http://httpbin.org/headers').headers
print(headers)
