import urllib3

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Define the URL to be accessed
url = 'https://www.example.com'

# Send a GET request to the specified URL
response = http.request('GET', url)

# Print the status code of the response
print(f"Status Code: {response.status}")

# Print the response data
print(f"Response Data: {response.data.decode('utf-8')}")
