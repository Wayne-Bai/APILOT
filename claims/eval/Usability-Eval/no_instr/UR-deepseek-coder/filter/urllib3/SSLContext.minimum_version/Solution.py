import urllib3
from urllib3 import util

# Create an SSL context with the minimum supported TLS version
ssl_context = util.ssl_.create_default_context()
ssl_context.minimum_version = util.ssl_.TLSVersion.MINIMUM_SUPPORTED

# Create a pool manager with the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Example request
response = http.request('GET', 'https://example.com')
print(response.data)
