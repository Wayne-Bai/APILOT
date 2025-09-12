
import ssl
from OpenSSL import SSL

# Create a new HTTPS connection using pyOpenSSL as the TLS backend
http = urllib3.PoolManager(
    cert_reqs='REQUIRED',
    ca_certs=CA_CERTS,
    tls_config=ssl.create_default_context()
)
