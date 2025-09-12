import urllib3

def enforce_content_length(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    received_content_length = int(response.headers.get('Content-Length', 0))

    # Check the Content-Length header in the response
    if received_content_length > 0 and received_content_length != response.size_read():
        raise ValueError("Content length mismatch. Body length does not match Content-Length header.")

    # Consume the response to release the connection
    response.read()
    response.release_conn()

# Test the function with a URL
enforce_content_length('http://example.com')
