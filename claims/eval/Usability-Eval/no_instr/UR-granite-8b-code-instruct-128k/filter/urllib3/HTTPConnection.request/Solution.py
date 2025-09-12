import urllib3

http = urllib3.PoolManager()
response = http.request(method, url)
