import urllib3

def read_response(url, amt):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Read the response body up to `amt` bytes
    data = response.data[:amt]
    response.release_conn()  # Always release the connection back to the pool
    return data

# Example usage
url = 'http://example.com'
bytes_to_read = 100
response_data = read_response(url, bytes_to_read)
print(response_data)
