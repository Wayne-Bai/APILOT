import urllib3

def send_http_request(method, url, headers=None, body=None):
    # Create a PoolManager instance to manage connections
    http = urllib3.PoolManager()

    try:
        # Send an HTTP request using the specified method and URL
        response = http.request(
            method=method,
            url=url,
            headers=headers,
            body=body
        )

        # Print the status code and response data
        print(f"Status: {response.status}")
        print("Response data:")
        print(response.data.decode('utf-8'))

    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP request failed: {e}")

# Example usage
method = 'GET'
url = 'http://example.com/api'
send_http_request(method, url)
