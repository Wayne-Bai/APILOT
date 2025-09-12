import urllib3
import ssl

# Create a custom context with lowest supported SSL/TLS version
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.minimum_version = ssl.TLSVersion.TLSv1

# Create an https pool manager with the custom context
https = urllib3.PoolManager(ssl_context=context)
