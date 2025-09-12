import urllib3

def get_connection_pool(pool_key):
    # Create a connection pool manager
    http = urllib3.PoolManager()
    
    # Return the connection pool based on the provided pool_key
    # Here, we're assuming a simplistic approach where the pool_key specifies host and port
    # Adjust this logic as per your application's needs.
    connection_pool = http.connection_pool(pool_key)
    
    return connection_pool
