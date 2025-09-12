import urllib3

# Assuming 'pool_key' is the key for the connection pool
pool = urllib3.connectionpool.HTTPConnectionPool(pool_key)
