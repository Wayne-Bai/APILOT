import urllib3

def get_connection_pool(base_url):
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Access the connection pool for the specified base URL
    connection_pool = http.connection_from_url(base_url)

    return connection_pool

# Example usage
if __name__ == "__main__":
    base_url = 'http://example.com'
    pool = get_connection_pool(base_url)
    print(pool)
