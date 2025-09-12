import urllib3

def send_request(method, url):
    """
    Send a request to the server using the HTTP request method.
    
    Args:
    method (str): The HTTP request method.
    url (str): The request URI.
    
    Returns:
    response: The server's response to the request.
    """

    # Create a PoolManager instance to manage a pool of connections
    http = urllib3.PoolManager()

    # Check if the URL is an absolute path
    if not url.startswith('http'):
        raise ValueError("The provided URL must be an absolute path")

    # Send the request to the server
    try:
        response = http.request(method, url)
        
        # Check if the request was successful
        response_status = response.status
        if response_status >= 200 and response_status < 300:
            print(f"Request successful. Status code: {response_status}")
        else:
            print(f"Request failed. Status code: {response_status}")
        
        return response
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
method = "GET"
url = "http://example.com"
response = send_request(method, url)
