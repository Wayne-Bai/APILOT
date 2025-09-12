import urllib3

def custom_redirect_logic(response, **kwargs):
    # Custom redirect logic can be implemented here
    if response.status == 302:
        # Example: Modify the redirect URL
        redirect_url = response.headers['Location']
        if 'example.com' in redirect_url:
            redirect_url = redirect_url.replace('example.com', 'newdomain.com')
        kwargs['redirect'] = False  # Prevent default redirect handling
        return redirect_url
    return None

def make_request(url, method='GET', body=None, headers=None):
    http = urllib3.PoolManager()
    response = http.request(
        method,
        url,
        body=body,
        headers=headers,
        redirect=False,  # Disable default redirect handling
        retries=False   # Disable automatic retries
    )

    # Handle custom redirect logic
    redirect_url = custom_redirect_logic(response)
    if redirect_url:
        response = http.request(
            method,
            redirect_url,
            body=body,
            headers=headers,
            redirect=False,
            retries=False
        )

    return response

# Example usage
url = 'http://example.com/api/resource'
response = make_request(url, method='GET')
print(response.status)
print(response.data)
