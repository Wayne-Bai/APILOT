Python
import urllib3
from urllib3 import poolmanager
from urllib3.connection import HTTPSConnection

class CustomHTTPSConnection(HTTPSConnection):
    def connect(self):
        super(CustomHTTPSConnection, self).connect()
        self.sock = self.ssl_context.wrap_socket(
            self.sock,
            server_hostname=self.host,
        )

poolmanager.pool_classes_by_scheme['https'] = urllib3.connectionpool.HTTPSConnectionPool
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    assert_hostname=True,
    ca_certs='path_to_your_ca_cert',  # insert the path to your CA certificate
    pool_cls=urllib3.connectionpool.HTTPSConnectionPool,
    conn_cls=CustomHTTPSConnection,
)

# Use the http object to send HTTP requests
response = http.request('GET', 'https://example.com')
