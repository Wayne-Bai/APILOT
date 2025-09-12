
import urllib3

# Define the function to get the ConnectionPool object
def get_pool(key):
    # Initialize the ConnectionPool class with the given pool key
    conn_pool = urllib3.connectionpool.ConnectionPool(key)
    return conn_pool
