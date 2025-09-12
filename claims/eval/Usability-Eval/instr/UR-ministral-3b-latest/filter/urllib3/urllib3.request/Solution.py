import urllib3

# Create a new PoolManager instance to avoid side effects
http = urllib3.PoolManager()

# Convenience, top-level request method
response = http.request('GET', 'https://www.example.com')
print(response.status, response.data)
