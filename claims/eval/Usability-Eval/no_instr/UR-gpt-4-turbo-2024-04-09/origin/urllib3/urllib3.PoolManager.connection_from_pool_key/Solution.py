import urllib3

def get_connection_pool(url):
    http = urllib3.PoolManager()
    return http.connection_from_url(url)

# Example usage
pool = get_connection_pool('http://example.com')
print(pool)
