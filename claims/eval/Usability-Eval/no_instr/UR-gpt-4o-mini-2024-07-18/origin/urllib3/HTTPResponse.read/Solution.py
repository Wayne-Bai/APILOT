import urllib3

def read_response_body(url, amt):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Read up to 'amt' bytes from the response body
    data = response.data[:amt]
    
    return data

# Example usage
url = 'http://example.com'
bytes_to_read = 100
response_data = read_response_body(url, bytes_to_read)
print(response_data)
