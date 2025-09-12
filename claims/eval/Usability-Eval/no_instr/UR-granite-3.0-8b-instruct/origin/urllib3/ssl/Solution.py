import urllib3

# Create a new HTTP connection pool
http = urllib3.PoolManager()

# Define the URL to connect to
url = "https://www.example.com"

# Send a GET request to the URL
response = http.request('GET', url)

# Print the response status code
print(response.status)

# Print the response text
print(response.data.decode())
