
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://www.example.com')

print(response.data)
