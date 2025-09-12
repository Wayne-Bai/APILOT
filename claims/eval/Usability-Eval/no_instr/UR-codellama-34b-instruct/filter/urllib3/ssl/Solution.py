import urllib3

# Create a PoolManager instance
pool = urllib3.PoolManager()

# Define the URL and payload for the request
url = 'https://www.example.com'
payload = {'key': 'value'}

# Send a GET request to the server
response = pool.request('GET', url, fields=payload)

# Print the response data
print(response.data)
