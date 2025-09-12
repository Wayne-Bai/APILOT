import urllib3

http = urllib3.PoolManager()

# Define a custom redirect logic
def redirect_handler(redirect_num, request, response, url):
    if redirect_num > 5:
        raise ValueError('Too many redirects')
    if response.status == 301 or response.status == 302:
        new_url = url.geturl()
        return new_url
    else:
        return None

# Perform the request with custom redirect logic
response = http.request('GET', 'http://example.com', redirect=redirect_handler)

# Print the response
print(response.data)
