import urllib3

def send_request(method, url):
    http = urllib3.PoolManager()
    response = http.request(method, url)
    return response.status, response.data

# Example usage:
status, data = send_request('GET', 'http://example.com/path')
print(f'Status: {status}, Data: {data}')
