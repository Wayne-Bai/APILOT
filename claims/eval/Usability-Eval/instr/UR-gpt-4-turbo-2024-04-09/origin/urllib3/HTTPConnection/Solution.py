import urllib3

def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=None):
    # Determine port if not provided
    if port is None:
        if ':' in host:
            host, port = host.split(':')
            port = int(port)
        else:
            port = 80  # Default HTTP port
    
    # Construct connection parameters dictionary
    connection_params = {
        'host': host,
        'port': port
    }
    
    # Include optional parameters if provided
    if timeout is not None:
        connection_params['timeout'] = timeout
    if source_address is not None:
        connection_params['source_address'] = source_address
    if blocksize is not None:
        connection_params['blocksize'] = blocksize

    # Create HTTPConnection object
    http = urllib3.HTTPConnectionPool(**connection_params)
    
    return http

# Example usage
http_conn = create_http_connection('example.com', timeout=10)
print(http_conn)
