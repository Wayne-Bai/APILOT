import urllib3

def send_request(url, method):
    # Create a PoolManager instance to handle connections
    http = urllib3.PoolManager()

    # Send the request and receive the response
    response = http.request(method, url)

    # Print the status and response data
    print(f"Status Code: {response.status}")
    print(f"Response Body: {response.data}")

# Example usage
url = "http://example.com"
method = "GET"
send_request(url, method)
