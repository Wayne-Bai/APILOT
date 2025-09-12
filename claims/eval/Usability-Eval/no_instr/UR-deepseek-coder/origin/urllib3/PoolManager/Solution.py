import urllib3

# Initialize the connection pool
http = urllib3.PoolManager()

def custom_redirect_logic(response):
    # Custom logic to handle redirects
    if response.status in (301, 302, 303, 307, 308):
        redirect_location = response.headers['Location']
        # Extract the request-uri portion of the URL
        request_uri = redirect_location.split('//')[1].split('/', 1)[1]
        return request_uri
    return None

def make_request(url, method='GET', body=None, headers=None):
    while True:
        # Perform the HTTP request
        response = http.request(method, url, body=body, headers=headers)
        
        # Check for redirects
        redirect_url = custom_redirect_logic(response)
        if redirect_url:
            url = redirect_url
        else:
            break
    
    return response

# Example usage
url = 'http://example.com/some/path'
response = make_request(url)
print(response.data.decode('utf-8'))
