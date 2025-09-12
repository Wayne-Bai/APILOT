import urllib3

def get_response_header_value(url, header_key):
    http = urllib3.PoolManager()
    
    # Make a request to the provided URL
    response = http.request('GET', url)
    
    # Retrieve the value of the specified header
    header_value = response.headers.get(header_key)
    
    # Cleanup the response
    response.release_conn()
    
    return header_value

# Example usage:
url = 'https://www.example.com'
header_key = 'Content-Type'
header_value = get_response_header_value(url, header_key)
print(f"The value of the '{header_key}' header is: {header_value}")
