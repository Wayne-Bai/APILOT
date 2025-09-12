import urllib3

def get_header_value(url, header_name):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    header_value = response.headers.get(header_name)
    return header_value

# Example usage:
# url = 'http://example.com'
# header_name = 'Content-Type'
# print(get_header_value(url, header_name))
