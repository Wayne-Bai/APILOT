import urllib3

def custom_redirect_logic(response, pool, method, redirect_url, **request_kw):
    # Custom logic to handle redirects
    if response.status == 302:
        # Extract the request-uri portion of the URL
        request_uri = redirect_url.split('?')[0]
        # Perform the request with the request-uri portion
        return pool.urlopen(method, request_uri, **request_kw)
    return response

def make_request(url, method='GET', **request_kw):
    http = urllib3.PoolManager()
    response = http.request(method, url, **request_kw)
    
    # Check for redirects and apply custom logic
    if response.status in (301, 302, 303, 307, 308):
        redirect_url = response.headers['Location']
        response = custom_redirect_logic(response, http, method, redirect_url, **request_kw)
    
    return response

# Example usage
url = 'http://example.com'
response = make_request(url)
print(response.data)
