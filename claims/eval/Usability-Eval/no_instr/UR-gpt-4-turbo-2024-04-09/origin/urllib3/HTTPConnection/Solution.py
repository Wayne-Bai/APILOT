import urllib3

# Create a function to handle the HTTP connection
def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=8192):
    # If no port specified, try to extract it from the host
    if port is None:
        if ':' in host:
            host, port = host.split(':')
            port = int(port)
        else:
            port = 80  # default HTTP port

    # Configure a PoolManager with the given source address if specified
    http = urllib3.PoolManager()
    if source_address:
        http.connection_pool_kw['source_address'] = source_address

    # Access the URL with optional timeout and blocksize
    try:
        # Construct the URL
        url = f"http://{host}:{port}"
        # Make the request
        response = http.request('GET', url, timeout=timeout, preload_content=False)

        # Read response data in chunks specified by blocksize
        try:
            while True:
                data = response.read(blocksize)
                if not data:
                    break
                print(data)  # Process or handle the data chunk
        finally:
            response.release_conn()  # Release the connection
    except urllib3.exceptions.NewConnectionError:
        print("Failed to connect to the server")
    except urllib3.exceptions.TimeoutError:
        print("The connection timed out")

# Example use of the function
create_http_connection('example.com', timeout=10, source_address=('192.168.1.1', 0), blocksize=1024)
