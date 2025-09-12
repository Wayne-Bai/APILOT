
import urllib3

# Specify the pool key
pool_key = 'my_pool_key'

# Get a ConnectionPool based on the provided pool key
pool = urllib3.PoolManager(connection_from_pool_key=pool_key)
