import urllib3
from urllib.parse import urlparse

# Create a connection pool
http = urllib3.PoolManager()

# Define the URL and specify only the request-uri portion
url = 'http://example.com/path/to/resource'
parsed_url = urlparse(url)
request_uri = parsed_url.path

# Set custom cross-host redirect logic
def custom_redirect(host, method, path, status, from_path=None, headers=None):
    """
    Custom cross-host redirect logic.
    In this example, we allow redirect for status 301 (Moved Permanently) to same host.
    """
    if status == 301:
        # Extract host from headers, in this case 'Location' header
        location_header = headers['Location']
        location_parsed_url = urlparse(location_header)
        if location_parsed_url.netloc == host:
            return location_parsed_url.path
    return None

# Perform an HTTP request with custom cross-host redirect logic
r = http.urlopen(
    method='GET',
    url=url,
    redirect_status_codes=[301, 302],
    headers={
        'Host': parsed_url.netloc
    },
    redirect=True,
    retries=3,
    preload_content=False
)

# Check for redirect
if 300 <= r.status <= 399:
    redirect_path = custom_redirect(parsed_url.netloc, 'GET', request_uri, r.status, from_path=request_uri, headers=r.headers)
    if redirect_path:
        # rebuild URL for redirect
        redirect_url = f"{parsed_url.scheme}://{parsed_url.netloc}{redirect_path}"
        # Make another request for redirect
        r = http.urlopen(
            method='GET',
            url=redirect_url,
            redirect_status_codes=[301, 302],
            headers={
                'Host': parsed_url.netloc
            },
            redirect=True,
            retries=3,
            preload_content=False
        )

print(r.data.decode('utf-8'))
