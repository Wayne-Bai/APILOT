import urllib3

def send_request(method, url):
    http = urllib3.PoolManager()
    response = http.request(method, url)
    return response.status, response.data

# Example usage:
status_code, response_data = send_request('GET', 'http://example.com')
print(f'Status code: {status_code}')
print(f'Response data: {response_data.decode()}')
