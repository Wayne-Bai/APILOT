import urllib3

http = urllib3.PoolManager()

url = 'https://example.com'
method = 'GET'

response = http.request(method, url)

print(response.data)
