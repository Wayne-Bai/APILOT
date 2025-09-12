import urllib3

def custom_redirect_request(pool, method, url, redirect_limit=10, **kwargs):
    if redirect_limit <= 0:
        raise urllib3.exceptions.MaxRetryError(pool, url)

    response = pool.urlopen(method, url, **kwargs)

    if response.status in (301, 302, 303, 307, 308):
        redirect_url = response.getheader('location')
        if redirect_url:
            # Extract the request-uri portion of the URL
            request_uri = urllib3.util.parse_url(redirect_url).request_uri
            return custom_redirect_request(pool, method, request_uri, redirect_limit=redirect_limit-1, **kwargs)

    return response

# Example usage:
http = urllib3.PoolManager()
response = custom_redirect_request(http, 'GET', '/example-endpoint')
print(response.data.decode('utf-8'))
