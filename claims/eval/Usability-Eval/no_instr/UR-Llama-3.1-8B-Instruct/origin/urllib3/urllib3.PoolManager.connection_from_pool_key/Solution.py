import urllib3

# Create a connection pool manager using the provided pool key
pool_manager = urllib3.PoolManager()

# Create a connection pool
pool = urllib3.connectionpool.ConnectionPool(
    manager=pool_manager,
    num_pools=10,  # specify the number of pools
    maxsize=10,  # specify the number of connections per pool
    block=True,
    timeout=5,
    retry=3,
    retries=[False, 'handler']
)
