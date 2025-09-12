
import urllib3
import ssl

# Create SSLContext for use with urllib3
context = ssl.create_default_context()

# Configure SSLContext for use with urllib3
context.check_hostname = True

# Set up urllib3 with SSLContext
urllib3_pool = urllib3.PoolManager(ssl_context=context)

# Now you can use urllib3_pool to make HTTPS requests securely
