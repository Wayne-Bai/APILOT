import urllib3

# Initialize a PoolManager instance to make requests.
http = urllib3.PoolManager()

# Define the URL to which the request will be made.
url = 'http://example.com/'

# Make a GET request to the server.
response = http.request('GET', url)

# Get the response data and status code.
data = response.data.decode('utf-8')
status_code = response.status

# Print the response status and data for debugging.
print("Status Code:", status_code)
print("Response Data:", data)

# Don't forget to release the connection.
response.release_conn()
