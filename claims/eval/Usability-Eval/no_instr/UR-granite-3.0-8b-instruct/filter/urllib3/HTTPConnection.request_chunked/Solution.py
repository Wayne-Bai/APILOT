import urllib3

http = urllib3.PoolManager()

data = b'This is a test message'
headers = {'Content-Type': 'text/plain', 'Transfer-Encoding': 'chunked'}

response = http.request('POST', 'http://example.com', fields={}, headers=headers, body_content=data)

print(response.status)
print(response.data.decode('utf-8'))
