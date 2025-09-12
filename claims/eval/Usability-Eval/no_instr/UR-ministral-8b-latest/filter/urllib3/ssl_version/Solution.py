import urllib3

# Set up SSL versions (optional, but suggested for security)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Example: Create an HTTP client with specific SSL versions
ssl_context = urllib3.util.ssl_.FallBackSSLContext()
ssl_context.minimum_version = ssl_context.DEFAULT_VERSION

client = urllib3.PoolManager(ssl_context=ssl_context)
