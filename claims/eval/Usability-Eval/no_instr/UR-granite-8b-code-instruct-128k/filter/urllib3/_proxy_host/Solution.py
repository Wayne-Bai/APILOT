import urllib3

http = urllib3.PoolManager()

proxy_url = 'http://user:password@hostname:port'

r = http.request('GET', 'http://example.com', headers={'Host': 'example.com'}, proxies=proxy_url)

print(r.status, r.data)