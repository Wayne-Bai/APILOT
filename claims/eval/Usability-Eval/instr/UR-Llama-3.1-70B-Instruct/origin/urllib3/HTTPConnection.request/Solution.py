import urllib3

def send_http_request(method, url):
    """
    Send an HTTP request to the server using the specified method and URL.

    Args:
        method (str): The HTTP method to use (e.g. 'GET', 'POST', 'PUT', etc.)
        url (str): The absolute path of the request URI

    Returns:
        response: The HTTP response object
    """

    # Create a PoolManager instance to manage the HTTP connection
    http = urllib3.PoolManager()

    # Send the HTTP request using the specified method and URL
    try:
        if method == 'GET':
            response = http.request('GET', url)
        elif method == 'POST':
            response = http.request('POST', url)
        elif method == 'PUT':
            response = http.request('PUT', url)
        elif method == 'DELETE':
            response = http.request('DELETE', url)
        else:
            raise ValueError(f'Unsupported method: {method}')

        # Print the response status code
        print(f'Response Status Code: {response.status}')

        # Return the response object
        return response

    except urllib3.exceptions.HTTPError as e:
        print(f'HTTP Error: {e}')
    except Exception as e:
        print(f'Error: {e}')

# Example usage
method = 'GET'
url = 'http://example.com'
response = send_http_request(method, url)
