
import urllib3

# Creating a new PoolManager instance to avoid shared side effects
http = urllib3.PoolManager()

# Using the new PoolManager instance to make a request
response = http.request('GET', 'http://httpbin.org/get')

print(response.status)
print(response.data)
