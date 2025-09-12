
import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Make a GET request to the specified URL
response = http.request('GET', 'https://www.example.com')

# Print the status code and response body
print(response.status_code)
print(response.data)
