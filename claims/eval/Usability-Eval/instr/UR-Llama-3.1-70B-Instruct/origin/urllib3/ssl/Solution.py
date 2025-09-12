import urllib3

# Suppress the warning related to insecure connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a pool manager to handle connections
pool = urllib3.PoolManager()

def make_get_request(url):
    """
    Makes an HTTPS GET request to the specified URL.
    
    Args:
    url (str): The URL to make the request to.
    
    Returns:
    str: The contents of the HTTP response.
    """
    try:
        # Make a GET request to the specified URL
        response = pool.request('GET', url)
        
        # Check if the request was successful
        if response.status == 200:
            return response.data.decode('utf-8')
        else:
            return None
    except Exception as e:
        print(f"Error making GET request: {e}")
        return None

def make_post_request(url, data):
    """
    Makes an HTTPS POST request to the specified URL with the given data.
    
    Args:
    url (str): The URL to make the request to.
    data (dict): The data to send with the request.
    
    Returns:
    str: The contents of the HTTP response.
    """
    try:
        # Make a POST request to the specified URL with the given data
        response = pool.request('POST', url, fields=data)
        
        # Check if the request was successful
        if response.status == 200:
            return response.data.decode('utf-8')
        else:
            return None
    except Exception as e:
        print(f"Error making POST request: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.example.com"
    
    # Make a GET request to the specified URL
    response = make_get_request(url)
    if response:
        print(response)
    
    # Make a POST request to the specified URL with some data
    data = {"key": "value"}
    response = make_post_request(url, data)
    if response:
        print(response)
