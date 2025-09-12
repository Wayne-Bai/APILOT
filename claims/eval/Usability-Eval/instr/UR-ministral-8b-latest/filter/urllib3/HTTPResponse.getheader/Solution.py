import urllib3

http = urllib3.PoolManager()

def get_header(headers, header_name):
    if header_name in headers:
        return headers[header_name]
    else:
        return None

response = http.request('GET', 'https://example.com')

print(get_header(response.headers, 'Content-Type'))
