
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://www.example.com')

# After sending the request, get the response
response = response.data

print(response)
