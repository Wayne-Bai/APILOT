import urllib3

# Create a pool manager instance
http = urllib3.PoolManager()

# Example GET request
response = http.request('GET', 'https://example.com')

# Print the response status code and data
print(f"Status Code: {response.status}")
print(f"Response Data: {response.data.decode('utf-8')}")
