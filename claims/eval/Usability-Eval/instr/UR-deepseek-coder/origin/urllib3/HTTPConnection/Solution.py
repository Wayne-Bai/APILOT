import urllib3

def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=8192):
    # Extract port from host if it's in the form host:port
    if ':' in host:
        host, port = host.split(':')
        port = int(port)
    else:
        port = port if port is not None else 80

    # Create an HTTPConnection instance
    connection = urllib3.HTTPConnection(
        host=host,
        port=port,
        timeout=timeout,
        source_address=source_address,
        blocksize=blocksize
    )

    return connection

# Example usage:
# connection = create_http_connection('example.com:8080', timeout=10, source_address=('127.0.0.1', 12345))
