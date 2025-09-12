import urllib3

# Creating a connection pool
def get_connection_pool(pool_key):
    """
    Create a urllib3.connectionpool.ConnectionPool based on the provided pool key.
    
    Args:
    pool_key (tuple): A tuple containing the scheme, host, and port.
    
    Returns:
    urllib3.connectionpool.ConnectionPool: A connection pool object.
    """
    pool = urllib3.connectionpool.ConnectionPool.fromkeys({
        pool_key: urllib3.connectionpool.ConnectionPool(
            host=pool_key[1],
            port=pool_key[2],
            scheme=pool_key[0],
            maxsize=10,
            block=True,
            timeout=10,
        )
    })
    return pool

# Usage
if __name__ == "__main__":
    # Define the pool key (scheme, host, port)
    pool_key = ('https', 'example.com', 443)
    
    # Get the connection pool
    conn_pool = get_connection_pool(pool_key)
    
    # Use the connection pool to make a request
    try:
        response = conn_pool.urlopen('GET', '/')
        print(response.status)
    except urllib3.exceptions.RequestError as e:
        print(f"Request failed: {e}")
