import urllib3

# Create a HTTPS connection object
http = urllib3.PoolManager()

# Make a GET request
response = http.request('GET', 'https://www.example.com')

# Print the response
print(response.data.decode('utf-8'))
