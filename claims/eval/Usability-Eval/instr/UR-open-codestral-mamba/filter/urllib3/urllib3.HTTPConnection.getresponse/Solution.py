import urllib3

http = urllib3.PoolManager()

# Assuming we're making a GET request to 'http://www.example.com'
response = http.request('GET', 'http://www.example.com')

# Now we can access the response data
print(response.data)
