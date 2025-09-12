import urllib3

http = urllib3.PoolManager()

url = 'https://www.example.com'
response = http.request('GET', url)

print(response.status)
print(response.data)
