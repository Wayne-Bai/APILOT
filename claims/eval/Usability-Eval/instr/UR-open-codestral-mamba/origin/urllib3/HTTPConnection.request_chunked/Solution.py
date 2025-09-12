import urllib3

http = urllib3.PoolManager()

url = "http://httpbin.org/post"
headers = {'Content-Type': 'application/json'}
data = '{"key": "value"}'

r = http.request('POST', url, headers=headers, body=data)

print(r.data)
