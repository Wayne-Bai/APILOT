import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'https://api.example.com')

print(response.status)
print(response.data)
