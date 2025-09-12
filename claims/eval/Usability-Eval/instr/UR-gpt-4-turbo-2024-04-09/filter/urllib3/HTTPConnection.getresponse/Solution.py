import urllib3

def get_server_response(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response

# Example usage
url = 'http://example.com'
response = get_server_response(url)
print('Status Code:', response.status)
print('Response Body:', response.data)
