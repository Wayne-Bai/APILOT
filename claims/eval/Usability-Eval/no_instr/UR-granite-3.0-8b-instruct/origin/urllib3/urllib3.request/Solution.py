import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Use the PoolManager instance for requests
response = http.request('GET', 'https://www.example.com')

# Print the response status code
print(response.status)
