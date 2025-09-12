from urllib3 import poolmanager, HTTPConnectionPool

# Create an HTTPConnectionPool instance with the specified redirect logic
http_pool = HTTPConnectionPool(
    # The host to connect to (cross-host redirect logic is required)
    host='example.com',
    # The port number to use for the connection
    port=443,
    # Enable cross-host redirects
    allow_redirects=True,
    # The maximum number of times to redirect
    max_redirects=5,
    # The timeout to use for the connection
    blocksize=8192,
    # Suppress the django debug toolbar
    debug_level=0,
)

# Perform an HTTP GET request using the pooled connection
def perform_http_request():
    # Get a connection from the pool
    conn = http_pool.get_conn()
    
    try:
        # Send a GET request to the specified URL
        r = conn.request('GET', 'https://example.com')
        
        # Get the response status
        status = r.status
        
        # Check the response status
        if status == 301:
            # If it's a redirect, extract the URI and send the request again
            new_uri = r.info().get('location')
            conn.request('GET', new_uri, headers=r.headers)
        elif status!= 200:
            # If the status is not OK, print the status
            print(f'Failed to retrieve the resource. status: {status}')
        
        # Get the response
        response = r.read()
        
        return response
    
    finally:
        # Close the connection
        conn.close()

# Perform the HTTP GET request and print the result
response = perform_http_request()
if response:
    print(response)
