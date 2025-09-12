import urllib3

# Create a connection pool
http = urllib3.PoolManager()

def make_request(url, method='GET', headers=None):
    # Parse the URL to get the URL port and host
    parsed_url = urllib3.util.urlsplit(url)

    # Extract the request-uri portion of the URL
    request_uri = urllib3.util.parse_url(parsed_url).path

    # Perform the HTTP request
    response = http.request(
        method,
        url,
        headers=headers
    )
    return response

# Example usage
url = 'http://example.com/some/path?query=param'
response = make_request(url)
print(response.data)
