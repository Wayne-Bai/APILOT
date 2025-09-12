import urllib3

# Create a connection pool
http = urllib3.PoolManager()

# Now `http` can be used to make requests to connect to Google App Engine
print("Connection manager created successfully!")
