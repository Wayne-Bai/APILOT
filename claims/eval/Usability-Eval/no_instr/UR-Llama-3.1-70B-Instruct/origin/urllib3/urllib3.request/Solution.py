import urllib3

# Create a new PoolManager instance to avoid side effects
http = urllib3.PoolManager()

def get_request(url):
    """
    A convenience, top-level request method.
    
    Args:
        url (str): The URL of the request.
    
    Returns:
        response: The response from the server.
    """
    try:
        # Send a GET request to the specified URL
        response = http.request('GET', url)
        
        # Check if the request was successful
        if response.status == 200:
            # Return the response content
            return response.data.decode('utf-8')
        else:
            # Raise an exception for unsuccessful requests
            response.raise_for_status()
    except urllib3.exceptions.RequestError as e:
        # Handle any request errors
        print(f"Request error: {e}")

def post_request(url, fields):
    """
    Send a POST request to the specified URL.
    
    Args:
        url (str): The URL of the request.
        fields (dict): A dictionary of key-value pairs to be sent in the request body.
    
    Returns:
        response: The response from the server.
    """
    try:
        # Send a POST request to the specified URL
        response = http.request('POST', url, fields=fields)
        
        # Check if the request was successful
        if response.status == 200:
            # Return the response content
            return response.data.decode('utf-8')
        else:
            # Raise an exception for unsuccessful requests
            response.raise_for_status()
    except urllib3.exceptions.RequestError as e:
        # Handle any request errors
        print(f"Request error: {e}")

# Example usage
if __name__ == "__main__":
    url = "http://example.com"
    fields = {"key": "value"}
    
    get_response = get_request(url)
    print(get_response)
    
    post_response = post_request(url, fields)
    print(post_response)
