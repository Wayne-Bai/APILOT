import urllib3

def make_request(url, method='GET', headers=None, body=None):
    # Create a new PoolManager instance for thread safety
    http = urllib3.PoolManager()

    # Set headers if provided
    if headers is None:
        headers = {}

    # Make the request using the specified parameters
    response = http.request(
        method,
        url,
        headers=headers,
        body=body
    )

    # Return the response data
    return response.data, response.status

# Example usage
url = 'http://httpbin.org/get'
data, status_code = make_request(url)
print(f"Status Code: {status_code}")
print(f"Response Data: {data.decode('utf-8')}")
