import ssl
import urllib3

# Create an SSL context
context = ssl.create_default_context()

# Disable SSL certificate verification (not recommended for production)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Create a connection pool with the SSL context
http = urllib3.PoolManager(ssl_context=context)

# Make a request using the pool
response = http.request('GET', 'https://example.com')
