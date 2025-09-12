import urllib3

def read_and_return_response_body(url, num_bytes):
    http = urllib3.PoolManager()
    response = http.request('GET', url, num_bytes=num_bytes)
    http.close()
    return response.data.decode('utf-8')  # Assuming the response is UTF-8 encoded

# Example usage
url = 'https://example.com'
num_bytes = 100
response_body = read_and_return_response_body(url, num_bytes)
print(response_body)
