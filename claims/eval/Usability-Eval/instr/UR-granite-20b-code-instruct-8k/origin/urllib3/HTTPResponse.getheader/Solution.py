import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://example.com')
header_value = response.getheader('Content-Type')
print(header_value)
