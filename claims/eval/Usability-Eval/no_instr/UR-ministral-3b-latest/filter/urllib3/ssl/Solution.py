from urllib3.util import PoolManager
import ssl
import socket

# Set up SSL context and pool manager
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
manager = PoolManager(timeout=5, ssl_context=ctx)

# Use the pool manager for making HTTPS requests
request = manager.request(
    'GET',
    'https://example.com', # replace with desired URL
)

# Print the response data
print(request.data)
