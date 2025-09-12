import urllib3

http = urllib3.PoolManager()
proxy = urllib3.ProxyHandler({'http': 'http://user:password@proxy.example.com:8080'})
http.proxies = {'http': proxy, 'https': proxy}

response = http.request('GET', 'https://www.example.com', headers={'User-Agent': 'Mozilla/5.0'})
