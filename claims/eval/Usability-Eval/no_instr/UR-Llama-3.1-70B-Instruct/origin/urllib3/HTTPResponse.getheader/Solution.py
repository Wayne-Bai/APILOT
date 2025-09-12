# Importing the required libraries
import urllib3

# Disable insecure warnings for HTTPS connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_header_value(url, header_name):
    """
    Returns the value of the given header from the response.

    Args:
    url (str): The URL to send a request to.
    header_name (str): The name of the header to retrieve.

    Returns:
    str: The value of the given header.
    """
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Send a request to the URL
    response = http.request('GET', url)

    # Get the headers from the response
    headers = response.getheaders()

    # Find the header value by name
    for header, value in headers:
        if header.lower() == header_name.lower():
            return value

    # If the header is not found, return None
    return None

# Example usage:
url = "http://www.example.com"
header_name = "Content-Type"
header_value = get_header_value(url, header_name)

if header_value:
    print(f"The value of '{header_name}' is: {header_value}")
else:
    print(f"'{header_name}' not found in the response headers.")
