import urllib3

def send_request(method, url):
    http = urllib3.PoolManager()
    response = http.request(method, url)
    return response

# Example usage:
method = 'GET'
url = 'http://example.com'
response = send_request(method, url)
print(response.status)
print(response.data)
