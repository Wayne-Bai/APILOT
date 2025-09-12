import urllib3

def get_connection_pool(pool_key):
    # Create a connection pool manager
    http = urllib3.PoolManager()
    
    # Return the connection pool based on the provided pool key
    return http.connection_from_url(pool_key)
