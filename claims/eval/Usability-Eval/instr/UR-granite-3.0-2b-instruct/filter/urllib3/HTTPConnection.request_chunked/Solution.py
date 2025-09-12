import urllib3

http = urllib3.PoolManager()

url = 'http://example.com'
data = b'This is the data to send'

response = http.request('POST', url, body=data, headers={'Content-Type': 'application/json'})

print(response.status, response.reason)
print(response.data.decode())
