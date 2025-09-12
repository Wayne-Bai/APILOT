import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Custom cross-host redirect logic function
def custom_redirect_request(url):
    # Parse the URL to get the request-uri
    request_uri = url.split('/', 3)[-1]  # Get everything after the hostname
    host = url.split('/')[2]  # Extract the hostname

    # Perform the HTTP request with custom headers if necessary
    response = http.request('GET', f'http://{host}/{request_uri}')

    # Return the response
    return response

# Example usage
url = 'http://example.com/path/to/resource'
response = custom_redirect_request(url)

# Print response status and data
print(response.status)
print(response.data)
