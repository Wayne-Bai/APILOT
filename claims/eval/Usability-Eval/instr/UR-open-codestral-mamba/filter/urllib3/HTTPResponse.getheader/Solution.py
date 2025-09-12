import urllib3

def get_header_value(url, header_name):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r.headers[header_name]

# Usage example
url = "https://example.com"
header_name = "Content-Type"
print(get_header_value(url, header_name))
