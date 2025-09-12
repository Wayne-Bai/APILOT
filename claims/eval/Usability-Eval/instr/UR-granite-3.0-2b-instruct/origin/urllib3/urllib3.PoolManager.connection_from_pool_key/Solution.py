import urllib3

# Create a new HTTP connection pool
http = urllib3.PoolManager()

# Get a connection pool based on the provided pool key
pool = http.get_pool('pool_key')
