import urllib3
from urllib3.util.ssl_ import create_urllib3_context

def create_ssl_context(minimum_version=None):
    # Create a new SSLContext with the specified minimum version
    context = create_urllib3_context()
    if minimum_version:
        context.minimum_version = minimum_version
    return context

# Example usage
ssl_context = create_ssl_context(minimum_version="TLSVersion.TLSv1_2")
http = urllib3.PoolManager(ssl_context=ssl_context)
