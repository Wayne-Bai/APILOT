import urllib3

# Create an SSL context
ssl_context = urllib3.SSLContext()

# Configure the SSL context
ssl_context.check_hostname = True
ssl_context.verify = True

# Now you can use this SSL context with urllib3
http = urllib3.PoolManager(ssl_context=ssl_context)
