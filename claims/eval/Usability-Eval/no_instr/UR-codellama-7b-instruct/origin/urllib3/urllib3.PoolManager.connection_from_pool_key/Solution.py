import urllib3

# Set the pool key
pool_key = "my_connection_pool"

# Get the ConnectionPool from the URL lib3
conn = urllib3.connectionpool(pool_key)

print("Connection Pool:", conn)
