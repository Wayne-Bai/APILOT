import urllib3

# Create an SSL context
ssl_context = urllib3.SSLContext()

# Configure the SSL context to verify SSL certificates
ssl_context.verify = "/path/to/ca_certificates.crt"

# Configure the SSL context to use the TLSv1.2 protocol
ssl_context.protocol = urllib3.SSLProtocol.TLSv1_2

# Configure the SSL context to not require client certificates
ssl_context.check_hostname = False
ssl_context.verify_mode = urllib3.SSLContext.VERIFY_NONE
