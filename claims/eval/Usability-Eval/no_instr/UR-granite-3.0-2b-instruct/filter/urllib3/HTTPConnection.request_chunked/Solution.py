import urllib3

http = urllib3.PoolManager()

data = b'Hello, world!'

response = http.request('POST', 'http://example.com', data=data, headers={'Content-Type': 'application/octet-stream'}, body_verbose=False)

print(response.read())
