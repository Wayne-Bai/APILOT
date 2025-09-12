import urllib3

http = urllib3.PoolManager()
http.start()

# Assuming proxy_pass is 'http://username:password@proxy_host:port'
http.request(
    'GET',
    'http://example.com',
    proxies={'http': 'http://username:password@proxy_host:port'}
)
