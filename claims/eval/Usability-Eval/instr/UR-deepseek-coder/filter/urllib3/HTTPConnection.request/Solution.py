import urllib3

def send_request(method, url, headers=None, body=None):
    http = urllib3.PoolManager()
    response = http.request(method, url, headers=headers, body=body)
    return response

# Example usage:
# response = send_request('GET', 'http://example.com/api/resource')
# print(response.status)
# print(response.data)
