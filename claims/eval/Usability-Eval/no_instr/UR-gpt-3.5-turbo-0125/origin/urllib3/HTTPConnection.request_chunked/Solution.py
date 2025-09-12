
import urllib3

http = urllib3.PoolManager()
url = 'http://example.com/api'
data = 'Your data here'

response = http.request('POST', url, body=data)
print(response.data)
