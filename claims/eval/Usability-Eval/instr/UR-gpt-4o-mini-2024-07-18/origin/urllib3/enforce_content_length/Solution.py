import urllib3

def fetch_with_content_length_check(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Check for Content-Length header
    content_length = response.headers.get('Content-Length')
    
    if content_length is not None:
        # Compare the value of Content-Length with the actual body length
        content_length = int(content_length)
        actual_length = len(response.data)
        
        if content_length != actual_length:
            raise ValueError(f"Content-Length mismatch: expected {content_length}, got {actual_length}")
    
    return response.data

# Example usage:
# try:
#     data = fetch_with_content_length_check('http://example.com')
#     print(data)
# except ValueError as e:
#     print(e)
