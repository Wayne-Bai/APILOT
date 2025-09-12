import urllib3

def fetch_with_content_length_check(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    # Check if Content-Length header is present
    content_length = response.headers.get('Content-Length')
    
    if content_length is not None:
        # Convert content_length to int for comparison
        content_length = int(content_length)
        
        # Check if the actual response length matches Content-Length
        if len(response.data) != content_length:
            raise ValueError(f"Content length mismatch: expected {content_length}, got {len(response.data)}")

    return response.data

# Example usage
try:
    data = fetch_with_content_length_check('http://example.com')
    print(data)
except ValueError as e:
    print(e)
