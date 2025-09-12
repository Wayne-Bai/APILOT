
import urllib3
from urllib3.contrib.pyopenssl import PyOpenSSLContext

# Create a pool manager with a PyOpenSSL context
pool_manager = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='path/to/ca_certs.pem',
    ssl_context=PyOpenSSLContext()
)

# Make a request using the pool manager
response = pool_manager.request('GET', 'https://example.com')
print(response.status)
