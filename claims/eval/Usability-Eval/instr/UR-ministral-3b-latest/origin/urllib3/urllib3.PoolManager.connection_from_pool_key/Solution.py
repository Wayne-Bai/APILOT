import urllib3

# Creating a ConnectionPool instance
pool = urllib3.poolmanager.PoolManager()

# Defining a connection URL
url = 'http://example.com'

# Creating a HTTP connection
connection = urllib3.connectionpool.ConnectionPool('http', url, port=80, num_pools=10)
result = connection.request('GET', '/')

print(result)
