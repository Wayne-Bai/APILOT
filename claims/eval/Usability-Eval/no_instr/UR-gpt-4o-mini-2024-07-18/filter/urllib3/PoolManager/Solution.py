import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the target URL and custom redirect logic
url = "http://example.com/somepath"
redirect_host = "http://another-example.com"  # Custom redirect host

try:
    # Perform a request to the initial URL
    response = http.request('GET', url)

    # Check for 3xx redirects
    if response.status in range(300, 400):
        # Parse the Location header to get the redirect URI
        redirect_uri = response.headers.get('Location', '')
        if redirect_uri:
            # Only send the request-uri portion, assuming it does not influence the host
            request_uri = redirect_uri.split('://')[-1]  # Removes the scheme
            # Handle custom host adding logic
            final_url = redirect_host + request_uri

            # Perform the redirect request
            redirect_response = http.request('GET', final_url)
            print(f'Redirect response status: {redirect_response.status}')
            print(f'Redirect response data: {redirect_response.data.decode()}')
        else:
            print("No Location header found for redirect.")
    else:
        print(f'Initial response status: {response.status}')
        print(f'Initial response data: {response.data.decode()}')

except Exception as e:
    print(f'An error occurred: {e}')
