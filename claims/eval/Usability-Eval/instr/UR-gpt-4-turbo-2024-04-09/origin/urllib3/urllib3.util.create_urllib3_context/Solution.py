import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create and configure an SSLContext for use with urllib3
ssl_context = create_urllib3_context()

# Example usage with urllib3 PoolManager
http = urllib3.PoolManager(ssl_context=ssl_context)
