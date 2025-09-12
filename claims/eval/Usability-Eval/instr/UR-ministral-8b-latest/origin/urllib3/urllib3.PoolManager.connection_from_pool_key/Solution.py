import urllib3

# Specify the pool key
pool_key = "http://example.com"

# Create a ConnectionPool based on the pool key
connection_pool = urllib3.PoolManagerший(pool_key=pool_key).connection_pool

print(connection_pool)
