# Import the required library
from urllib3 import PoolManager

# Create an HTTP connection instance with a host, port number, and timeout
http_connection = PoolManager(timeout=10.0, maxsize=10)

# Define a function to establish a connection with the host
def connect_to_host(host, port=80):
    """
    Establish an HTTP connection with the given host and port.

    Args:
        host (str): The hostname or IP address to connect to.
        port (int): The port number to use. Defaults to 80.

    Returns:
        response: An HTTP response object, or None if the request fails.
    """
    try:
        # Get the absolute URL to pass to urllib3
        absolute_url = f"http://{host}:{port}"

        # Make a request to the URL and return the response
        return http_connection.request('GET', absolute_url)
    except Exception as e:
        # Log any exceptions that occur during the request
        print(f"Error connecting to host: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    host = "www.example.com"
    port = 80

    response = connect_to_host(host, port)

    # Check if the response was successful
    if response is not None:
        print(f"Status Code: {response.status}")
    else:
        print("Failed to connect to host")
