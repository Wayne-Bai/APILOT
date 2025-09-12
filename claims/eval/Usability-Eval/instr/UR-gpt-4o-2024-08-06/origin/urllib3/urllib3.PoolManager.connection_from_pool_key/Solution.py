import urllib3
from urllib3.util import make_headers

def get_connection_pool(url, pool_key, maxsize=10):
    # Initialize a PoolManager
    http = urllib3.PoolManager(maxsize=maxsize)

    # Create headers if needed, otherwise, you can pass None
    headers = make_headers(user_agent="my-app")

    # Acquire a connection pool from the pool manager
    connection_pool = http.connection_from_url(url)

    # Optional: Store the pool with a custom key
    pool_key.setdefault(pool_key, connection_pool)

    return connection_pool

# Usage example:
url = 'http://example.com'
pool_key_dict = {}
connection_pool = get_connection_pool(url, pool_key_dict)

print(connection_pool)
