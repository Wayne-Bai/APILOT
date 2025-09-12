import urllib3
from urllib3 import PoolManager

# Create a new PoolManager instance to avoid side effects
http = PoolManager()

def make_request(url, method='GET', fields=None, headers=None, **kwargs):
    """
    A convenience, top-level request method.

    :param url: The URL to request
    :param method: The method to use for the request (e.g. GET, POST, PUT, DELETE)
    :param fields: A dictionary of data to send with the request
    :param headers: A dictionary of headers to send with the request
    :param **kwargs: Additional keyword arguments to pass to the request method
    """
    try:
        # Use the PoolManager instance to make the request
        response = http.request(method, url, fields=fields, headers=headers, **kwargs)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the response data
        return response.data
    
    except urllib3.exceptions.HTTPError as errh:
        # Handle HTTP errors
        print(f"HTTP Error: {errh}")
        return None
    
    except urllib3.exceptions.ConnectionError as errc:
        # Handle connection errors
        print(f"Error Connecting: {errc}")
        return None
    
    except Exception as err:
        # Handle any other errors
        print(f"Other error: {err}")
        return None


# Example usage:
url = "http://httpbin.org/ip"
response_data = make_request(url)

print(response_data)

url = "http://httpbin.org/post"
data = {'key': 'value'}
response_data = make_request(url, method='POST', fields=data)

print(response_data)
