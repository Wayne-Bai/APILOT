import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://httpbin.org/get')

if response.headers.get('Content-Length'):
    content_length = int(response.headers.get('Content-Length'))
    if len(response.data) != content_length:
        raise ValueError('Content length mismatch')
