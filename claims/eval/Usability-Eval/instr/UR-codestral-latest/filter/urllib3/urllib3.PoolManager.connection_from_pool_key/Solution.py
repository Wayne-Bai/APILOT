import urllib3

# Define your pool key
pool_key = 'your_pool_key'

# Create a custom connection pool manager
http = urllib3.PoolManager()

# Create a connection pool
connection_pool = http.connection_from_url(pool_key)
