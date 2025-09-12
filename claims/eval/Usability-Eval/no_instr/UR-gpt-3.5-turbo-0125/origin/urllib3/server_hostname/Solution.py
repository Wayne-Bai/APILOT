
import urllib3

http = urllib3.PoolManager()

url = 'http://www.example.com'
response = http.request('GET', url)

print(response.data)
