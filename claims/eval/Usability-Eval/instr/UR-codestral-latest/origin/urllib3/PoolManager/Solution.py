import urllib3

# Create a connection pool manager
http = urllib3.PoolManager()

# Define the URL
url = 'http://www.example.com/path'

# Parse the URL to get the request-uri
parsed_url = urllib3.util.parse_url(url)
request_uri = parsed_url.request_uri

# Perform the request
response = http.request(
    "GET",
    request_uri,
    headers={"Host":parsed_url.host}
)

# Print the response
print(response.status)
print(response.data)
