
import urllib3

# Create a SSLContext object
ctx = urllib3.util.make_ssl_context()

# Configure the SSLContext to use the desired protocol version
ctx.protocol = 'TLSv1_2'  # or 'TLSv1_3' for TLS 1.3

# Configure the SSLContext to use a specific certificate and private key
ctx.certfile = '/path/to/your/certificate.crt'
ctx.keyfile = '/path/to/your/private_key.pem'

# Configure the SSLContext to trust only specific certificates
ctx.trust_store.append('/path/to/a/certificate.crt')
ctx.trust_store.append('/path/to/another/certificate.crt')

# Use the configured SSLContext with urllib3
http = urllib3.PoolManager(ssl_context=ctx)
response = http.request('GET', 'https://example.com')
