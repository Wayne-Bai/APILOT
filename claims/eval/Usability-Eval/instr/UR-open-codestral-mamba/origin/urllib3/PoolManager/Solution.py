import urllib3

# Create a PoolManager
http = urllib3.PoolManager()

# For getting a connection from the pool and perform an HTTP request
def get_connection(url):

    # Extracting the Scheme and netloc from url
    parsed_url = urllib3.util.parse_url(url)

    # Specify all the raw details
    request_method = 'GET'
    request_uri = parsed_url.scheme + "://" + parsed_url.netloc

    # Get the connection from the pool and perform an HTTP request
    resp = http.request(request_method, request_uri)

    # Custom cross-host redirect logic
    # This part of the code should be implemented if the server/request know how to
    # handle such redirects. We assume such logic will be present at the server side.

    # Now, return the response
    return resp

# Test the function with a URL
url = 'http://example.com'
response = get_connection(url)
print(response.data)
