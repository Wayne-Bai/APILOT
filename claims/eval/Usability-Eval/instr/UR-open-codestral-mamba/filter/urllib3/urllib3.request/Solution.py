import urllib3

def send_request(url, method='GET', fields=None):
    http = urllib3.PoolManager()
    response = http.request(method=method, url=url, fields=fields)
    return response.data

# Usage
print(send_request('http://example.com'))  # GET request by default
print(send_request('http://example.com', method='POST', fields={'key': 'value'}))  # POST request
