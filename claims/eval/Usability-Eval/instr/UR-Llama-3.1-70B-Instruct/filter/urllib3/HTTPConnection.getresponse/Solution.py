import urllib3

def get_server_response(url):
    """
    Sends a GET request to the server and returns the HTTP response.

    Args:
        url (str): The URL of the server.

    Returns:
        HTTPResponse: The response from the server.
    """
    # Create a PoolManager instance to manage a pool of connections
    http = urllib3.PoolManager()

    try:
        # Send a GET request to the server
        response = http.request('GET', url)

        # Return the HTTP response
        return response
    except urllib3.exceptions.HTTPError as e:
        # Handle any HTTP errors
        print(f"HTTP Error: {e}")
        return None
    except urllib3.exceptions.RequestError as e:
        # Handle any request errors
        print(f"Request Error: {e}")
        return None
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "http://example.com"
    response = get_server_response(url)

    if response:
        # Print the HTTP status code
        print(f"Status Code: {response.status}")

        # Print the HTTP headers
        print("Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Print the response data
        print("Data:")
        print(response.data.decode('utf-8'))
