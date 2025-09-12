
import urllib3

url = 'http://example.com'
proxy = 'http://proxy-server:8080'

http = urllib3.ProxyManager(proxy)
response = http.request('GET', url)
print(response.status, response.data)
