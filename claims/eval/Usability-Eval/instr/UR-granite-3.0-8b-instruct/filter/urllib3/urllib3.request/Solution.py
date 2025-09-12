import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Use the PoolManager instance to send a request
response = http.request('GET', 'http://example.com')
