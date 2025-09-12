import urllib3

def get_header_value(url, header_name):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.headers.get(header_name)

# Example usage:
url = 'http://example.com'
header_name = 'Content-Type'
header_value = get_header_value(url, header_name)
print(f"The value of the '{header_name}' header is: {header_value}")
