
import urllib3

def create_connection(host, port=None, timeout=None, source_address=None, blocksize=None):
    """
    Creates an HTTPConnection instance to a specified host and port.

    Args:
        host (str): The hostname or IP address of the server.
        port (int, optional): The port number for the connection. If not given, the default HTTP port (80) is used.
        timeout (float, optional): The maximum time in seconds to wait for a response. If not given, the global default timeout setting is used.
        source_address (tuple, optional): A tuple of (host, port) to use as the source address for the connection.
        blocksize (int, optional): The buffer size in bytes for sending a file-like message body. Defaults to 64 KB.

    Returns:
        HTTPConnection: An instance of the HTTPConnection class.
    """
    if port is None:
        # Extract the port from the host string if it has the form host:port, else use the default HTTP port (80)
        port = urllib3.util.parse_url(host).port or 80

    http_connection = urllib3.HTTPConnection(host, port=port, timeout=timeout, source_address=source_address)
    return http_connection
