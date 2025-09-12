import urllib3

def get_server_hostname(pool_manager):
    try:
        # Get the server name from the connection pool manager
        server_hostname = pool_manager.connection_pool_kw['server_hostname']
        return server_hostname
    except KeyError:
        # If the key is not found, return None
        return None

# Example usage
http = urllib3.PoolManager()
hostname = get_server_hostname(http)
print(hostname)
