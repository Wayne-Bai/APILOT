import urllib3

# Create a connection pool
http = urllib3.PoolManager()

def make_request(hostname, path):
    # Perform the HTTP request
    response = http.request('GET', f'http://{hostname}{path}')

    # Extract the request-uri portion of the URL
    request_uri = response.geturl()

    return response, request_uri

# Example usage
hostname = 'www.example.com'
path = '/path/to/resource'

response, request_uri = make_request(hostname, path)
print("Response Status:", response.status)
print("Request URI:", request_uri)
