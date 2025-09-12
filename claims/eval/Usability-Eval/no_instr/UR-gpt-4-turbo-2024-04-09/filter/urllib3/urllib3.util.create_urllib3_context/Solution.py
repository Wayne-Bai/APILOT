import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create and configure SSL context for urllib3
def create_ssl_context():
    # Create a default SSL context
    ssl_context = create_urllib3_context()

    # Configuration can be added here. For example:
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    return ssl_context

# Usage of the SSL context in a PoolManager
http = urllib3.PoolManager(ssl_context=create_ssl_context())
