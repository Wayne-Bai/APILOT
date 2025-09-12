import urllib3

def custom_request(url, redirect_limit=5):
    # Create a connection pool manager
    http = urllib3.PoolManager()

    # Parse the original URL to extract just the request URI path
    parsed_url = urllib3.util.parse_url(url)
    request_uri = parsed_url.request_uri

    # Initial request
    response = http.request('GET', url, redirect=False)

    # Custom redirection logic with limit
    redirect_count = 0
    while redirect_count < redirect_limit and response.status in (301, 302, 303, 307, 308):
        # Get the location header and update the request URI
        redirect_url = response.get_redirect_location()
        if not redirect_url:
            break

        parsed_redirect_url = urllib3.util.parse_url(redirect_url)
        request_uri = parsed_redirect_url.request_uri

        # Perform the new request using just the URI
        response = http.request('GET', request_uri, redirect=False)
        redirect_count += 1

    return response

# Example usage
if __name__ == "__main__":
    url = 'http://example.com'
    response = custom_request(url)
    print('Final URL:', response.geturl())
    print('Status:', response.status)
    print('Response Body:', response.data.decode('utf-8'))
