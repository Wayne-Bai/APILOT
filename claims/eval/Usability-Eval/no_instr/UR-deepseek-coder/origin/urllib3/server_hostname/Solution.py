import urllib3

def get_server_hostname(http):
    try:
        # Get the hostname from the connection pool manager
        hostname = http.connection_pool_manager.host
        return hostname
    except AttributeError:
        return None

# Example usage
http = urllib3.PoolManager()
hostname = get_server_hostname(http)
print(f"Hostname of the server: {hostname}")
