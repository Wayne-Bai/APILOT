import urllib3
from urllib3.util import Retry
from urllib3.exceptions import TimeoutError

def establish_http_connection(host, port=80, timeout=10, source_address=None, blocksize=8192):
    """
    Establishes an HTTP connection with the specified host, port, timeout, source address, and blocksize.

    Args:
        host (str): The hostname or IP address of the HTTP server.
        port (int): The port number of the HTTP server. Defaults to 80.
        timeout (int): The timeout in seconds for blocking operations. Defaults to 10.
        source_address (tuple): A tuple containing the source host and port for the HTTP connection. Defaults to None.
        blocksize (int): The buffer size in bytes for sending a file-like message body. Defaults to 8192.

    Returns:
        A tuple containing the HTTPConnectionPool instance and a flag indicating if the connection was successful.
    """
    try:
        # Create an HTTPConnectionPool instance
        if source_address:
            pool = urllib3.HTTPConnectionPool(host, port, timeout=timeout, source_address=source_address, blocksize=blocksize)
        else:
            pool = urllib3.HTTPConnectionPool(host, port, timeout=timeout, blocksize=blocksize)

        # Try to make a request to the HTTP server
        pool.request('HEAD', '/', retries=Retry(3))

        # If no exception occurred, return the pool instance and True
        return pool, True

    except TimeoutError:
        # If a TimeoutError occurred, return None and False
        print("Connection timed out!")
        return None, False

    except Exception as e:
        # If any other exception occurred, print the error message and return None and False
        print(f"An error occurred: {e}")
        return None, False

# Example usage
if __name__ == "__main__":
    host = "www.example.com"
    port = 80
    timeout = 10
    source_address = ("localhost", 8080)  # Optional source address
    blocksize = 8192

    pool, connection_successful = establish_http_connection(host, port, timeout, source_address, blocksize)

    if connection_successful:
        print(f" Successfully established connection with {host}:{port}")
    else:
        print(f"Failed to establish connection with {host}:{port}")
