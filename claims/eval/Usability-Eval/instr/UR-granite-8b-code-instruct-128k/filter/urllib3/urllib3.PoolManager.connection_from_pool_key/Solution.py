import urllib3

def get_connection_pool(pool_key):
    http = urllib3.PoolManager()
    return http
