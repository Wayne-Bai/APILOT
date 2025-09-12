import urllib3
http = urllib3.PoolManager()
response = http.request('GET', 'http://httpbin.org/get')
header = response.headers['content-type']
print(header)
