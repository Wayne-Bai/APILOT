
import urllib3

# Create a new SSL context with default settings
ssl_context = urllib3.util.ssl_.create_default_context()

# Configure the SSL context to use TLS v1.2 and validate certificates
ssl_context.set_protocol(urllib3.util.ssl_.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = urllib3.util.ssl_.CERT_REQUIRED

# Return the configured SSL context
return ssl_context
