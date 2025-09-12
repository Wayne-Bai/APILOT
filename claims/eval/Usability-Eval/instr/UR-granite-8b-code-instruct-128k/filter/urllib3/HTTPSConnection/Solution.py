import urllib3
from urllib3.contrib.pyopenssl import PyOpenSSLContext

class MySecureHTTPConnection(urllib3.connection.HTTPConnection):
    """A subclass of HTTPConnection that uses SSL for communication with secure servers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = PyOpenSSLContext(ssl_version=urllib3.util.ssl_.DEFAULT_SSL_VERSION)

http = urllib3.PoolManager(connections=MySecureHTTPConnection)
response = http.request('GET', 'https://www.example.com/')
print(response.data)
