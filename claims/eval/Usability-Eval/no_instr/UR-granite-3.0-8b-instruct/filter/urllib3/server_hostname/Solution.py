import urllib3

def create_pool_manager(hostname):
    if hostname is None:
        pool_manager = urllib3.PoolManager()
    else:
        http = urllib3.PoolManager(hostname=hostname)
        pool_manager = http.pool_manager

    return pool_manager
