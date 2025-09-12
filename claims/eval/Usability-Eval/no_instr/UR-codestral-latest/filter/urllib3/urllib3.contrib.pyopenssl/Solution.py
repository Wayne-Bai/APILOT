import urllib3

http = urllib3.PoolManager()

# Create a connection pool
connection_pool = urllib3.poolmanager.PoolManager(num_pools=5, cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

# Make a request
response = connection_pool.request('GET', 'https://example.com')
