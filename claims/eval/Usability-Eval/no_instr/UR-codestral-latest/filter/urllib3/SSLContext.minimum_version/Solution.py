import urllib3
from urllib3 import PoolManager
from urllib3.util.ssl_ import create_urllib3_context

# Create SSL context with the lowest supported TLS version
ssl_context = create_urllib3_context(
    ssl_version=urllib3.util.ssl_.PROTOCOL_SSLv3
)

# Create a PoolManager with the SSL context
http = PoolManager(ssl_context=ssl_context)

# Now you can use the 'http' object to make requests using the lowest supported TLS version
response = http.request('GET', 'https://example.com')
