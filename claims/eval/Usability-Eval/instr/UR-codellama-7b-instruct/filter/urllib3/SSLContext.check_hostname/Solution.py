
import urllib3

# Create a SSLContext object with hostname checking disabled
context = urllib3.SSLContext()
context.check_hostname = False

# Set verify mode to CERT_OPTIONAL or CERT_REQUIRED
context.verify_mode = urllib3.util.ssl_.CERT_OPTIONAL

# Create a SSLSocket object using the SSLContext and server hostname
socket = urllib3.SSL.SSLSocket(context, server_hostname="example.com")

# Perform TLS handshake with the server
socket.do_handshake()
