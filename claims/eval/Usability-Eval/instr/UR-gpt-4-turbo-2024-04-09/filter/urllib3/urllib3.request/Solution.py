import urllib3

def make_request(url):
    # Create a new PoolManager instance to avoid side effects of using a shared instance
    http = urllib3.PoolManager()
    
    # Make the request
    response = http.request('GET', url)
    
    # Return the response data
    return response.data

# Example usage
if __name__ == "__main__":
    url = 'http://example.com'
    data = make_request(url)
    print(data)
