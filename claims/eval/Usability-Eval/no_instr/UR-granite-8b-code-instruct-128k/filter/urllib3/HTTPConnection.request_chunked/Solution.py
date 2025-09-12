import urllib3

http = urllib3.PoolManager()

response = http.request(
    'POST',
    'https://httpbin.org/anything',
    body='{"key": "value"}',
    headers={'Content-Type': 'application/json'},
    encode_chunked=True,
)

print(response.data.decode('utf-8'))
