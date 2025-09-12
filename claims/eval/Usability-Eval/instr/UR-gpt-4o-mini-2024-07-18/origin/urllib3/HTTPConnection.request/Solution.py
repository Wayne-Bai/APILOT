import urllib3

def send_request(method, url):
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Send the request
    response = http.request(method, url)

    # Return the response data
    return response.data

# Example usage
method = 'GET'  # eg. 'GET', 'POST', etc.
url = 'http://example.com'
response_data = send_request(method, url)
print(response_data)
