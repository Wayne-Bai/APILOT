import urllib3

http = urllib3.PoolManager()

def custom_redirect(response):
    # Custom redirect logic here
    # For example, let's just return the response if it's not a redirect
    if response.status != 300 and response.status != 301:
        return response

    # Extract the request-uri portion of the URL
    request_uri = response.url.split('//')[-1].split('?')[0]

    # Make a new request to the request-uri
    new_response = http.request('GET', request_uri, headers=response.headers)

    # Return the new response
    return new_response

# Make an HTTP request with custom cross-host redirect logic
response = http.request('GET', 'https://example.com/path?redirect=https://example.com/other-path', headers={'User-Agent': 'my-app/0.0.1'})
response = custom_redirect(response)

# Print the response
print(response.data)
