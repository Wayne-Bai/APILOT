import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Send a request to the server
response = http.request('GET', 'http://example.com')

# Return the HTTPResponse instance
# In an actual implementation, you would return this from a function or use it as needed.
print(response)
