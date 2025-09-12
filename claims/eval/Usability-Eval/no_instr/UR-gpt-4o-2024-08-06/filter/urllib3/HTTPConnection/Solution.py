import urllib3

def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=8192):
    # Initialize a connection pool manager
    http = urllib3.PoolManager()

    # Construct the full URL with the host and port
    if port is None:
        parts = host.split(':')
        if len(parts) == 2 and parts[1].isdigit():
            url = host
        else:
            url = f"{host}:80"
    else:
        url = f"{host}:{port}"

    # Prepare connection parameters
    connection_params = {
        'timeout': timeout,
        'source_address': source_address,
        'blocksize': blocksize
    }

    # Additional parameter adjustments if required
    if timeout is not None:
        connection_params['timeout'] = timeout
    
    if source_address is not None:
        connection_params['source_address'] = source_address
    
    # Simulate a connection attempt (useful for illustration, usually PoolManager handles connection reuse)
    print(f"Creating HTTP connection to {url} with parameters:")
    print(connection_params)

    # Make a sample request to demonstrate connection (GET request)
    response = http.request('GET', f"http://{url}", timeout=timeout)
    
    # Status code is for example purposes; in real life, you handle the response properly
    print(f"Response status: {response.status}")

# Example usage:
create_http_connection('example.com', timeout=10, source_address=('0.0.0.0', 0))
