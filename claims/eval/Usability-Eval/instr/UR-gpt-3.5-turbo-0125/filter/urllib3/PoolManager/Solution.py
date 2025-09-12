
import urllib3

http = urllib3.PoolManager()
url = 'http://www.example.com/path/to/file'

response = http.request('GET', url, redirect=False, headers={'Host': 'www.example.com'})

print(response.data)
