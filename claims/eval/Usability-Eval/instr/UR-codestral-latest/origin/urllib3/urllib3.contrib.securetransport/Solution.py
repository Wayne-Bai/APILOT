import urllib3
from urllib3 import PoolManager
import ssl

# Load macOS native SSL library
if 'darwin' in sys.platform.lower():
    from OpenSSL import SSL
    from urllib3.util.ssl_ import create_urllib3_context

    class CustomSSLContext(ssl.SSLContext):
        def __init__(self):
            super().__init__(SSL.TLS_METHOD)

        def wrap_socket(self, sock, *args, **kwargs):
            ssl_sock = SSL.Connection(self, sock)
            return ssl_sock

    create_urllib3_context = CustomSSLContext
    PoolManager = urllib3.poolmanager.PoolManager

# Create a pool manager with the macOS SSL fix
http = PoolManager(ssl_context=create_urllib3_context(), cert_reqs='CERT_REQUIRED', ca_certs='cert.pem')

# Making a GET request
response = http.request('GET', 'https://example.com')
print(response.data)
