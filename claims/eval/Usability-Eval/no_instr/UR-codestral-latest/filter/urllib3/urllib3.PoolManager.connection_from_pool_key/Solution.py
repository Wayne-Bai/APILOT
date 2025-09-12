import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Define the pool key (host)
host = "www.example.com"

# Create a ConnectionPool using the pool key
connection_pool = http.connection_from_url(host)

