import urllib3
from urllib3 import HTTPResponse

# Initialize a PoolManager instance, which is the most convenient way to make requests
http = urllib3.PoolManager()

def get_header_value(url, header_name):
    """
    Returns the value of a specific header for the response from the given URL.

    Args:
        url (str): The URL to make the request to.
        header_name (str): The name of the header to retrieve the value for.

    Returns:
        str: The value of the specified header, or None if the header is not present in the response.
    """
    try:
        # Make a GET request to the given URL
        response: HTTPResponse = http.request('GET', url)
        
        # Check if the response was successful
        if response.status == 200:
            # Get the headers from the response
            headers = response.getheaders()
            
            # Iterate over the headers to find the one we're looking for
            for header, value in headers:
                if header.lower() == header_name.lower():
                    return value
        return None
    except urllib3.exceptions.RequestError as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
url = 'http://httpbin.org'
header_name = 'Content-Type'
header_value = get_header_value(url, header_name)
print(f"The value of '{header_name}' header is: {header_value}")
