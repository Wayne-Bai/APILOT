
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://www.example.com/', headers={'User-Agent': 'myCustomUserAgent'})

print(response.status)
print(response.data)
