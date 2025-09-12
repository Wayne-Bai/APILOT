import urllib3

# Create an HTTP client instance
http = urllib3.PoolManager()

# URL example
url = "http://example.com"

# Send a GET request to the URL
response = http.request('GET', url)

# Check if the request was successful
if response.status == 200:
    print("Request was successful!")
    print("Response body:", response.data.decode('utf-8'))
else:
    print("Failed to connect:", response.status, response.reason)
