import urllib3

# Create a PoolManager object that will manage HTTP connections for us
http = urllib3.PoolManager()

# Define the method and URL
method = 'GET'
url = 'http://www.example.com'

# Send the request
r = http.request(method, url)

# Print the response data
print(r.data)

# The r object also contains the following information:
# - r.status: the HTTP status code returned by the server (e.g. 200)
# - r.headers: the headers returned by the server as a dictionary-like object
# - r.data: the response data (e.g. HTML content, JSON, etc.)
