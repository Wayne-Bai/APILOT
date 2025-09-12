import urllib3
from urllib3.poolmanager import PoolManager

# Set up a connection pool for handling URIs
class CustomHTTPConnectionPool(PoolManager):
    def connect(self, method, url, *args, **kwargs):
        https = urllib3.PoolManager()
        response = https.request(method, url, *args, **kwargs)
        return response

# You can then use the CustomHTTPConnectionPool when you need connections
pool = CustomHTTPConnectionPool(network)
