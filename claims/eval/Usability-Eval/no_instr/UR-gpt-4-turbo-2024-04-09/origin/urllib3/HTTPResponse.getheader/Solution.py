import urllib3

def get_header_value(url, header_name):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.headers.get(header_name)

# Example usage
url = 'http://example.com'
header_name = 'Content-Type'
header_value = get_header_value(url, header_name)
print(f"Value of header '{header_name}' is: {header_value}")
