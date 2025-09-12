import urllib3

# Create a connection pool that only allows SSL connections
pool = urllib3.PoolManager(
    ssl_version=urllib3.TLSv1_2,
)

# Connect to the server using the connection pool
conn = pool.connection_from_host("www.example.com", port=443)

# Check if the server supports SSL/TLS version 1.2 or higher
if conn.ssl_version() < urllib3.TLSv1_2:
    print("SSL/TLS version not supported")
else:
    print("SSL/TLS version supported")
