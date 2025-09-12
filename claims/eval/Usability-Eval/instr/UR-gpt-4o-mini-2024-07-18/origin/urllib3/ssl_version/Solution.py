import urllib3

# Create a PoolManager with default settings
http = urllib3.PoolManager()

# Example URL to connect to (change it to your target URL)
url = 'https://example.com'

# Make a request to the URL
response = http.request('GET', url)

# Print the response status and data
print("Response status:", response.status)
print("Response data:", response.data.decode('utf-8'))
