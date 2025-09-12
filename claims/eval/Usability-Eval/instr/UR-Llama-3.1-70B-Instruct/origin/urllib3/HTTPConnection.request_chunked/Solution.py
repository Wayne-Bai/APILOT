import urllib3

# Disable the InsecureRequestWarning if you're working with unverified SSL certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def chunked_request(url, data):
    # Create a pool manager with the URL
    http = urllib3.PoolManager()
    
    # Initialize the headers with Transfer-Encoding as chunked
    headers = urllib3.util.make_headers(keep_alive=True, accept_encoding=True)
    headers['Transfer-Encoding'] = 'chunked'
    
    # Initialize the request with the headers
    req = urllib3.request.RequestEncodedBody(
        method='POST', 
        url=url, 
        headers=headers, 
        fields=data, 
        encode_multipart=False,
        preload_content=False
    )
    
    # Make the request with chunked encoding
    r = http.urlopen(req, preload_content=False)
    
    # Manually read and print the chunks
    while True:
        chunk = r.read(1024)
        if not chunk:
            break
        print(chunk.decode('utf-8'))

# Usage example
url = 'http://httpbin.org/post'
data = {'key': 'value'}
chunked_request(url, data)
