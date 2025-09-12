import urllib3

# Function to create an HTTP connection
def create_http_connection(host, port=None, timeout=10.0, source_address=None, blocksize=8192):
    # Configure the pool manager
    http = urllib3.PoolManager(timeout=timeout, blocksize=blocksize)
    
    # If port is not defined, check if we can extract it from the host string
    if port is None:
        if ':' in host:
            host, port = host.split(':')
            port = int(port)
        else:
            # Default HTTP port (80)
            port = 80
    
    # Construct URL to open the connection
    url = f"http://{host}:{port}"
    
    # Configure headers, may include the source address if necessary
    headers = {}
    if source_address:
        headers['Source-Address'] = f"{source_address[0]}:{source_address[1]}"
    
    # Make a request to the provided host:port
    response = http.request('GET', url, headers=headers)
    
    # Return the response status and data
    return response.status, response.data

# Example of using the function
status, data = create_http_connection('example.com:80')
print(f"HTTP Status: {status}")
print(f"Response Data: {data.decode('utf-8')}")
