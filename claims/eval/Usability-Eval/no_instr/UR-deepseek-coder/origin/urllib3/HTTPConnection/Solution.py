import urllib3

def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=8192):
    # Extract port from host if it's in the form host:port
    if ':' in host:
        host, port = host.split(':')
        port = int(port)
    
    # Use default HTTP port (80) if no port is provided
    if port is None:
        port = 80
    
    # Create an HTTPConnection instance
    http = urllib3.HTTPConnectionPool(
        host=host,
        port=port,
        timeout=timeout,
        source_address=source_address,
        blocksize=blocksize
    )
    
    return http

# Example usage:
# http_connection = create_http_connection('example.com:8080', timeout=10)
