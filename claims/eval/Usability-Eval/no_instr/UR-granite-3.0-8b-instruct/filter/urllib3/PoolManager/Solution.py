import urllib3

http = urllib3.PoolManager()

url = "http://example.com/path?query=param"

# Extract the request-uri portion of the URL
request_uri = urllib3.util.parse_url(url).path

# Create a custom cross-host redirect logic function
def custom_redirect_logic(response, location):
    # Add your custom logic here
    # For example, you can check if the location is within the same host
    # and return True if it is, otherwise return False
    return location.startswith("http://example.com")

# Get a connection from the pool and perform an HTTP request with custom cross-host redirect logic
response = http.request('GET', request_uri, redirects=custom_redirect_logic)

# Print the response
print(response.data.decode())
