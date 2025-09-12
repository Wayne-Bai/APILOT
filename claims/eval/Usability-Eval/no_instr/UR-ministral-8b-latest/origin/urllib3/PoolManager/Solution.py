import urllib3

# Set up connection pool
http = urllib3.PoolManager()
headers = {'User-Agent': 'my-app/0.0.1'}

# Define the function to handle cross-host redirects
class RedirectingHTTPAdapter(urllib3.ProxyManagerHTTPAdapter):
    def process_response(self, request, response, **kw):
        if response.status >= 300 and response.status < 400:
            # Attempt to redirect to the URL specified by the 'Location' header
            if 'Location' in response.headers:
                redirected_url = response.headers['Location']
                return urllib3.util.recode.urlparse(redirected_url)._replace(netloc=request.netloc).geturl()
        return response

# Create a custom HTTP request function
def perform_request_with_redirects(url, request_uri):
    full_url = f"{url.rstrip('/')}/{request_uri.lstrip('/')}"
    adapter = RedirectingHTTPAdapter()
    response = http.request('GET', url, headers=headers, redirect=True, proxies={'https': adapter}, retries=False)
    return response.data, response.status

# Example usage
url = 'https://example.com'
request_uri = 'resource/path'
data, status_code = perform_request_with_redirects(url, request_uri)
print(f"Received response with status code {status_code}")
print(f"Response data:\n{data}")
