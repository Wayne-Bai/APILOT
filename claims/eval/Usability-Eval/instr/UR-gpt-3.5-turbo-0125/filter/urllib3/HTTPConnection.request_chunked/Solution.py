
import urllib3

http = urllib3.PoolManager()
url = 'https://api.example.com'
data = {'key': 'value'}

r = http.request('POST', url, body=data, headers={'Content-Type': 'application/json'})
print(r.data)
