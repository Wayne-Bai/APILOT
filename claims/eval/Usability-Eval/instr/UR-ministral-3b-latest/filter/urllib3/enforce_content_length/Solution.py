import urllib3

http = urllib3.PoolManager()

response = http.request(
    'GET',
    'http://example.com',
    headers={'Content-Length': '123'}
)

print(response.content.strip())

if len(response.data) != int(response.headers['Content-Length']):
    raise ValueError('Content length mismatch.')

