
import urllib3

url = "http://www.example.com/"
method = "GET"

http = urllib3.PoolManager()
response = http.request(method, url)

print(response.data.decode('utf-8'))
