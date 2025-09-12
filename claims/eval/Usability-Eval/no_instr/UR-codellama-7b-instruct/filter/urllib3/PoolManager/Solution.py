
import urllib3

def make_request(url, method="GET", headers=None, body=None):
    # Create a connection pool manager
    manager = urllib3.PoolManager()

    # Build the request object
    request = urllib3.Request(url, method, headers, body)

    # Get a connection from the pool
    conn = manager.connection_from_host(request.get_full_url())

    # Perform the HTTP request
    response = conn.urlopen(request)

    # Return the response object
    return response
