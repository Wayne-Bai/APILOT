import urllib3

# Create an SSLContext instance
ssl_context = urllib3.SSLContext()

# Configure the SSLContext instance
ssl_context.check_hostname = True
ssl_context.verify_mode = urllib3.security.verify_basic
