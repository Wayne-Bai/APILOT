import urllib3

def send_request(url):
    """
    Send an HTTP request to the specified URL and return the response.
    
    Args:
        url (str): The URL to send the request to.
    
    Returns:
        urllib3.response.HTTPResponse: The response from the server.
    """
    
    # Initialize the HTTP manager
    http = urllib3.PoolManager()
    
    try:
        # Send the request and get the response
        response = http.request('GET', url)
        
        # Print the status code of the response
        print(f"Status code: {response.status}")
        
        # Print the data received from the server
        print(f"Response data: {response.data}")
        
        return response
    
    except urllib3.exceptions.RequestError as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")
        return None

# Usage
url = "http://example.com"
send_request(url)
