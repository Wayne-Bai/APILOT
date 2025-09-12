# Import the required library
import urllib3

def get_server_response(url):
    """
    Sends a GET request to the provided URL and returns the HTTP response.
    
    Args:
    url (str): The URL to send the request to.
    
    Returns:
    HTTPResponse: The server's response to the request.
    """
    
    # Create a PoolManager instance to manage connections
    http = urllib3.PoolManager()
    
    try:
        # Send a GET request to the provided URL
        response = http.request('GET', url)
        
        # Return the server's response
        return response
    
    except urllib3.exceptions.HTTPError as e:
        # Handle any HTTP-related errors
        print(f"HTTP error occurred: {e}")
        return None
    
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "http://example.com"
    response = get_server_response(url)
    
    if response is not None:
        print(f"Server responded with status code {response.status}")
        print(f"Server's response: {response.data}")
