import urllib3

http = urllib3.PoolManager()

data = b"This is the data to be sent"

headers = {
    'Content-Type': 'text/plain',
    'Transfer-Encoding': 'chunked'
}

response = http.request('POST', 'http://example.com', fields={}, headers=headers, body_content=data)

print(response.status)
print(response.data.decode('utf-8'))
