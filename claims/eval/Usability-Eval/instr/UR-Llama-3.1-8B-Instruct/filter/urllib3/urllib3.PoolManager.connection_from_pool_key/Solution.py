import urllib3

http = urllib3.PoolManager()
pool_key = "example_key"

def get_connection_pool(pool_key):
    """
    Get a urllib3.connectionpool.ConnectionPool based on the provided pool key.

    Args:
        pool_key (str): The key for the connection pool.

    Returns:
        urllib3.connectionpool.ConnectionPool: The connection pool for the given key.
    """
    return http._create_pool(pool_key)

connection_pool = get_connection_pool(pool_key)
print(connection_pool)
