import urllib3

def make_request_with_custom_redirect_logic(base_url, target_url, path, headers=None):
    # Creating a PoolManager instance to handle connection pooling and thread safety
    http = urllib3.PoolManager()

    # Performing the initial request
    response = http.request('GET', base_url + path, headers=headers, redirect=False)

    if response.status in [301, 302, 303, 307, 308]:
        # In case of redirect, parse the Location header to handle cross-host redirect
        redirect_url = response.get_redirect_location()

        # Custom logic to verify if the redirect URL matches the target_url domain
        if urllib3.util.url.parse_url(redirect_url).host == urllib3.util.url.parse_url(target_url).host:
            # Only sending the request-uri portion to the new host (path and query)
            redirect_path = urllib3.util.url.parse_url(redirect_url).request_uri
            response = http.request('GET', target_url + redirect_path, headers=headers, redirect=False)
        else:
            print("Redirect to a different host is not allowed.")
    else:
        print("No redirect needed.")

    return response

# Example usage
base_url = 'http://example.com'
target_url = 'http://otherexample.com'
path = '/initial/request'
response = make_request_with_custom_redirect_logic(base_url, target_url, path)

# Print response data
print(response.status)
print(response.data.decode('utf-8'))
