import urllib3

# Create a urllib3.connectionpool.ConnectionPool object using the provided pool key
pool_key = "example_key"
pool = urllib3.connectionpool.ConnectionPool(key=pool_key)
