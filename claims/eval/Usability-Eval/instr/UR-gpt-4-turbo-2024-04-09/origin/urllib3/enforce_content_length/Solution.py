import urllib3
from urllib3.exceptions import ProtocolError

def fetch_url_with_content_length_check(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Check if 'Content-Length' header is present
    content_length = response.headers.get('Content-Length')
    if content_length is not None:
        content_length = int(content_length)
        actual_length = len(response.data)
        
        if actual_length != content_length:
            raise ProtocolError(f"Content length mismatch: Expected {content_length}, got {actual_length}")
    
    return response.data

# Example usage:
url = "http://example.com"
try:
    data = fetch_url_with_content_length_check(url)
    print(data)
except ProtocolError as e:
    print(f"An error occurred: {e}")
