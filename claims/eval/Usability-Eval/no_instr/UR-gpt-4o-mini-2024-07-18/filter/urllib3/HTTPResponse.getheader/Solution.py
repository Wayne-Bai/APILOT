import urllib3

def get_header_value(url, header_name):
    # Create a PoolManager instance
    http = urllib3.PoolManager()
    
    # Make a request to the URL
    response = http.request('GET', url)
    
    # Return the value of the specified header
    return response.headers.get(header_name)

# Example usage
url = 'http://example.com'
header_name = 'Content-Type'
header_value = get_header_value(url, header_name)
print(f"The value of '{header_name}' is: {header_value}")
