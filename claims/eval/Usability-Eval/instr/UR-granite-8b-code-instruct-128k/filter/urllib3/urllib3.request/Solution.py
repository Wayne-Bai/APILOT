import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Make a request using the new instance
response = http.request('GET', 'https://www.example.com')

# Do something with the response
print(response.data.decode('utf-8'))
