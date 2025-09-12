import urllib3
http = urllib3.PoolManager()
res = http.request('GET', 'https://example.com', ssl_version='TLSv1.2',)
