import urllib3

def custom_redirect_request(host, port=None, method='GET', url='/', headers=None, body=None, retries=3, redirect_white_list=None):
    if redirect_white_list is None:
        redirect_white_list = set()
    
    # Define the connection pool
    if port:
        http = urllib3.HTTPConnectionPool(host, port=port)
    else:
        http = urllib3.HTTPConnectionPool(host)
    
    # Prepare the response
    response = http.urlopen(method, url, body=body, headers=headers, assert_same_host=False, retries=retries)

    # Handle redirects
    num_redirects = 0
    while response.status in (300, 301, 302, 303, 307) and num_redirects < retries:
        redirect_url = response.get_redirect_location()
        if not redirect_url:
            break
        
        # Only proceed with redirects that are within the whitelist
        redirect_host = urllib3.util.url.parse_url(redirect_url).host
        if redirect_host in redirect_white_list:
            u = urllib3.util.url.parse_url(redirect_url)
            if u.host == host:
                # Same host so redirect is alright to follow
                response = http.urlopen(method, u.request_uri, body=body, headers=headers, assert_same_host=False)
            else:
                # New host in white list, create a new connection pool
                http = urllib3.HTTPConnectionPool(u.host)
                response = http.urlopen(method, u.request_uri, body=body, headers=headers, assert_same_host=False)
        else:
            print(f"Redirect to {redirect_host} not allowed.")
            break
        num_redirects += 1

    return response

# Usage example
if __name__ == "__main__":
    host = 'example.com'
    redirect_whitelist = {'example.com', 'www.example.com'}
    res = custom_redirect_request(host, url='/', redirect_white_list=redirect_whitelist)
    print(res.status)
    print(res.data)
