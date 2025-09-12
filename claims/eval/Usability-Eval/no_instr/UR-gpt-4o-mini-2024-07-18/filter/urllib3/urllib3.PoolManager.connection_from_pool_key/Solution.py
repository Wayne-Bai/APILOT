import urllib3

def get_connection_pool(pool_key):
    # Create a PoolManager instance which will manage the connection pools
    http = urllib3.PoolManager()

    # Initialize a new connection pool based on the provided pool key
    connection_pool = http.connection_pool(pool_key)

    return connection_pool

# Example usage:
pool_key = 'http://example.com'
connection_pool = get_connection_pool(pool_key)
