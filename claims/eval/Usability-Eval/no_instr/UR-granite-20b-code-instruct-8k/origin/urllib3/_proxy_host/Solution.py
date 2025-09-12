import urllib3
http = urllib3.ProxyManager('http://proxied-server.com')
response = http.request('GET', '/')
print(response.status)
print(response.data.decode('utf-8'))
