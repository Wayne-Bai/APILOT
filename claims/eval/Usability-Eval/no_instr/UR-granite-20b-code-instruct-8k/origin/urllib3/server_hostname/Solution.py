import urllib3

hostname = 'example.com'
http = urllib3.PoolManager(host=hostname)
response = http.request('GET', '/')
print(response.status)
print(response.data)
