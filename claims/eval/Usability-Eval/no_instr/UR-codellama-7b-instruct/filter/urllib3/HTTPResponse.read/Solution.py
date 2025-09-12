
import urllib3

# Create a new HTTP connection object
http = urllib3.PoolManager()

# Perform a GET request on the URL
response = http.request('GET', 'https://www.example.com')

# Read the response body as text
body = response.data.decode('utf-8')

print(body)
