import urllib3

# Assuming the pool key is "http://example.com"
pool_key = "http://example.com"

# Creating a PoolManager instance
http = urllib3.PoolManager()

# Getting the connection pool based on the pool key
conn_pool = http.connection_pool_for(pool_key)

print(conn_pool)
