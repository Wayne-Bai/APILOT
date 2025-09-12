import urllib3
from urllib3.util import Retry
from urllib3.exceptions import ProtocolError

def fetch_url(url):
    http = urllib3.PoolManager()
    
    # Perform the request
    response = http.request('GET', url)
    
    # Check if the Content-Length header is present
    content_length_header = response.headers.get('Content-Length')
    if content_length_header:
        content_length = int(content_length_header)
        actual_length = len(response.data)
        
        if content_length != actual_length:
            raise ValueError(f"Content length mismatch: Expected {content_length} but got {actual_length}")
        
        return response.data
    else:
        raise ValueError("Content-Length header is missing")

# Example URL to fetch
url = "http://example.com"
try:
    data = fetch_url(url)
    print(data)
except Exception as e:
    print(e)
