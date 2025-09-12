import urllib3
from urllib3.util import ssl_

# Create a custom HTTPSConnectionPool with specific SSL version limits
class MyHTTPSConnectionPool(urllib3.HTTPSConnectionPool):
    def __init__(self, *args, **kwargs):
        # Ensure SSLv23_METHOD is used which allows negotiation within the allowed range
        kwargs['ssl_version'] = ssl_.PROTOCOL_TLS
        
        # Pass minimum_version to SSL context
        self.min_tls_version = ssl_.TLSVersion.MINIMUM_SUPPORTED
        
        super().__init__(*args, **kwargs)

    def _new_conn(self):
        # Create a new connection with the appropriate TLS minimal version
        conn = super()._new_conn()
        if isinstance(conn.sock, ssl_.SSLContext):
            # Set the minimum version of TLS allowed
            conn.sock.minimum_version = self.min_tls_version
        return conn

# Usage of the custom HTTPSConnectionPool with min TLS version
base_url = 'https://example.com'
pool = MyHTTPSConnectionPool(base_url)
response = pool.request('GET', '/')
print(response.status)
print(response.data)
