import urllib3

# Create a custom HTTPConnectionPool
class MyHTTPConnectionPool(urllib3.pool.PoolManager):
    def _make_new_connection(self, host, port, **kwargs):
        return MyHTTPSConnection(host, port, **kwargs)

class MyHTTPSConnection(urllib3.connection.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        self.tls = urllib3.ssl_.SSLContext(ssl.PROTOCOL_TLSv1_2)
        super(MyHTTPSConnection, self).__init__(*args, **kwargs)
        self.tls.load_verify_locations(cafile='/path/to/ca-bundle.crt')

    def connect(self, full_url, timeout=None):
        httplib = super(MyHTTPSConnection, self).connect(full_url, timeout)
        return httplib.send(self.tls.wrap_socket(httplib.getresponse(), ssl=True))

# Create an HTTPConnectionPool with the custom pool manager
http = MyHTTPConnectionPool(pool_size=10, max_retries=5)

# Use the HTTPConnectionPool to make requests
response = http.request('GET', 'https://example.com', headers={'User-Agent': 'my-app/0.0.1'})
