import urllib3

class ContentLengthError(Exception):
    pass

def get_content_with_length_check(url):
    http = urllib3.PoolManager()
    
    with http.request('GET', url, preload_content=False) as response:
        content_length = response.headers.get('Content-Length')
        
        if content_length is not None:
            content_length = int(content_length)
        
        body_content = response.data
        actual_length = len(body_content)
        
        if content_length is not None and content_length != actual_length:
            raise ContentLengthError(f"Expected content length {content_length}, but got {actual_length}.")
        
        return body_content

# Example Usage
try:
    url = 'http://example.com'
    content = get_content_with_length_check(url)
    print(content)
except ContentLengthError as e:
    print(f"Content length mismatch: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
