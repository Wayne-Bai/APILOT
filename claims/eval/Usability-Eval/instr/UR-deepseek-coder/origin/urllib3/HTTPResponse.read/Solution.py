import urllib3

def read_response_body(url, amt=None):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    if amt is None:
        return response.data
    else:
        return response.data[:amt]

# Example usage:
# url = 'http://example.com'
# body = read_response_body(url, amt=100)
# print(body)
