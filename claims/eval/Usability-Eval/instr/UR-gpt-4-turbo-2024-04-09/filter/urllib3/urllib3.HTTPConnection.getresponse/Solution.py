import urllib3

# Create an instance of the PoolManager
http = urllib3.PoolManager()

# Specify the URL
url = "http://example.com"

# Make a GET request to fetch data from the server
response = http.request('GET', url)

# Print the response data
print(response.data)
