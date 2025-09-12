import urllib3

# Initialize a PoolManager instance
http = urllib3.PoolManager()

# Specify the URL you want to send a request to
url = 'http://example.com/'

# Send a GET request to the server
response = http.request('GET', url)

# Print response status and data
print(f"Status: {response.status}")
print(f"Data: {response.data.decode('utf-8')}")
