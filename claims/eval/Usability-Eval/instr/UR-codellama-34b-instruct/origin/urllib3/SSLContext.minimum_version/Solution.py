
import ssl

# Create a new SSL context
context = ssl.create_default_context()

# Set the minimum supported version of TLS to 1.2
context.maximum_version = ssl.TLSVersion.MINIMUM_SUPPORTED

# Use the SSL context with urllib3
http = urllib3.PoolManager(ssl_context=context)
