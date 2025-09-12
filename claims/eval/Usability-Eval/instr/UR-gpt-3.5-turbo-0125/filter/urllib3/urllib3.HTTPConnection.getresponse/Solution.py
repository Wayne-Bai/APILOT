
import urllib3

url = 'http://www.example.com'
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.data)
