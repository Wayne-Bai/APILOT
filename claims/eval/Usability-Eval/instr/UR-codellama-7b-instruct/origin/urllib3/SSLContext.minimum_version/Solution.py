
import urllib3

# Set the minimum supported version of TLS
minimum_version = urllib3.TLSVersion.MINIMUM_SUPPORTED

# Create a SSLContext object with the minimum supported version of TLS
ssl_context = urllib3.SSLContext(minimum_version)

# Use the SSLContext object to create a HTTPSConnection object
https_connection = urllib3.HTTPSConnection('example.com', ssl_context=ssl_context)
