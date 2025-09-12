import urllib3
from urllib3 import connectionpool

# Create a new pool manager which is capable of managing connections
http = urllib3.PoolManager()

# A sample get request
response = http.request('GET', 'http://www.google.com')

print(response.status)
print(response.data)
