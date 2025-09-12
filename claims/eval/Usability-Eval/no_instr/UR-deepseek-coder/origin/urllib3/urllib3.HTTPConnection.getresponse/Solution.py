import urllib3

# Create a PoolManager instance to make requests.
http = urllib3.PoolManager()

# Define the URL you want to request.
url = "http://example.com"

# Make a GET request to the URL.
response = http.request('GET', url)

# Print the response data.
print(response.data.decode('utf-8'))
