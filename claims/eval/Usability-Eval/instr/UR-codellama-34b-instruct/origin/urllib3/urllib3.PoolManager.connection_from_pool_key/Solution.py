
import urllib3

# Create a connection pool based on the provided pool key
pool_key = 'my-pool'
pool = urllib3.connectionpool.ConnectionPool(pool_key)

# Set up the connection pool with your desired options
pool.set('connection_timeout', 10)
pool.set('max_connections', 5)

# Get a connection from the pool
conn = pool.get()
