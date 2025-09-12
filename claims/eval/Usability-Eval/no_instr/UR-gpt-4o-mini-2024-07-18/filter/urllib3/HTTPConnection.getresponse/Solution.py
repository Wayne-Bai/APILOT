import urllib3

# Create a PoolManager instance to handle connections
http = urllib3.PoolManager()

# Make a request to a URL
url = 'http://example.com'  # Replace with your target URL
response = http.request('GET', url)

# The response is an HTTPResponse instance
print('Status:', response.status)
print('Data:', response.data.decode('utf-8'))

# Always remember to release the connection back to the pool
response.release_conn()
