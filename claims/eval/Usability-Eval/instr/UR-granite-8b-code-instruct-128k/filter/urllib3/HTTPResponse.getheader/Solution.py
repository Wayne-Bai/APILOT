import urllib3
http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')
header_value = response.headers.get('header_name')
print(header_value)
