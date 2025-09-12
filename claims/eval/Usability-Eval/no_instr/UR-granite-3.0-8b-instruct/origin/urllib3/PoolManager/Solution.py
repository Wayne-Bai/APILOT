import urllib3

def custom_redirect_handler(response, request, context):
    if response.status == 301 or response.status == 302:
        new_location = response.headers.get('Location')
        if new_location and not new_location.startswith(request.url):
            return urllib3.http.RedirectResponse(new_location, request, context)
    return None

http = urllib3.PoolManager(redirect_handler=custom_redirect_handler)

response = http.request('GET', 'http://example.com/path/to/resource', fields={})

print(response.data.decode())
