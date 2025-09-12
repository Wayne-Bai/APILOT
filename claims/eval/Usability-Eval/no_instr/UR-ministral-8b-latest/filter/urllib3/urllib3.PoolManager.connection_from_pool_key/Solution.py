import urllib3

# Create a connection pool with a specified key
connection_pool = urllib3.ConnectionPool(
    key='my_pool',
    manager=urllib3.Manager(ssl_context=urllib3.ssl.EffectivesslContext()),
    ssl=True  # or set False for non-ssl connections
)

# Example of using the connection pool to make a request
http = urllib3.PoolManager(connection_pool=connection_pool)
response = http.request("GET", "http://example.com")
print(response.data)
