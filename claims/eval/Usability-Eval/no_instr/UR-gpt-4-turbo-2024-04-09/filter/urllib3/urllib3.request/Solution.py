import urllib3

def make_request(url):
    # Creating a new PoolManager instance to avoid side effects
    http = urllib3.PoolManager()
    
    # Making a request to the specified URL
    response = http.request('GET', url)
    
    return response

# Example usage
url = 'http://example.com'
response = make_request(url)
print(response.status)
print(response.data)
