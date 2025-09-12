import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://example.com')

if 'Content-Length' in response.headers and len(response.data) != int(response.headers['Content-Length']):
    raise ValueError('Content-Length header and body length do not match')
