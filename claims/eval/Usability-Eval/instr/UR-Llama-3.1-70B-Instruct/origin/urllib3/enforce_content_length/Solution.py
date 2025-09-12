import urllib3

# Disable the warning about the SSL certificate verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def enforce_content_length_checking(pool_manager, url):
    response = pool_manager.urlopen('GET', url, preload_content=False)
    
    # Check if the Content-Length header is present
    if 'Content-Length' in response.headers:
        expected_length = int(response.headers['Content-Length'])
        
        # Read the response body and calculate its length
        content = response.read()
        actual_length = len(content)
        
        # Check if the actual length matches the expected length
        if actual_length!= expected_length:
            raise ValueError(f"Content length mismatch: Expected {expected_length} bytes, but got {actual_length} bytes")
        
    return content

# Create a connection pool manager
pool_manager = urllib3.PoolManager()

# Use the function to make a request
url = 'http://example.com'
try:
    content = enforce_content_length_checking(pool_manager, url)
    print(content)
except urllib3.exceptions.HTTPError as e:
    print(f"An HTTP error occurred: {e}")
except ValueError as e:
    print(f"A value error occurred: {e}")
