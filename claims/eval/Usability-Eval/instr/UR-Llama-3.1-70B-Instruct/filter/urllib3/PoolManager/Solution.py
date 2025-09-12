import urllib3
from urllib3 import util

# Create a connection pool
http = urllib3.PoolManager(
    num_pools=10,
    maxsize=10,
    retries=3,
    timeout=5.0,
)

def custom_cross_host_redirects(resp, **kw):
    """Custom cross-host redirect logic"""
    return resp.status in (301, 302)

def make_request():
    """Make an HTTP request with custom cross-host redirect logic"""
    # Get a connection from the pool
    url = 'http://example.com/path'
    method = 'GET'
    Fields = util.make_headers(
        keep_alive=True,
        accept_encoding=True,
    )
    request = http.request_encode_url(
        method=method, 
        url=url,
        fields=Fields,
        retries=3, 
        redirect=True,
        headers={'User-Agent': 'test'}, 
        encode_multipart=False,
        preload_content=False,
    )
    
    # Check if the request is redirected to another host
    if custom_cross_host_redirects(request):
        # Follow the redirect manually
        new_url = request.headers['Location']
        print(f'Redirected to {new_url}')
        
        # Perform a new request to the redirected URL
        new_request = http.request_encode_url(
            method=method, 
            url=new_url,
            fields=Fields,
            retries=3, 
            redirect=True,
            headers={'User-Agent': 'test'}, 
            encode_multipart=False,
            preload_content=False,
        )
        return new_request
  
    return request

# Call the make_request function
request = make_request()
print(request.status)
