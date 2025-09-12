
import urllib3

# Create a connection pool with a maximum of 10 connections
http = urllib3.PoolManager(num_pools=10)

# Perform a GET request to a specific URL
url = 'http://www.example.com'
r = http.request('GET', url)

print(r.status, r.data)
