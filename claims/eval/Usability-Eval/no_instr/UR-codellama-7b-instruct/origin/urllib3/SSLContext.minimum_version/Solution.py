
import urllib3

# Set the minimum supported TLS version to TLS 1.0
urllib3.util.ssl_.TLSVersion.MINIMUM_SUPPORTED = urllib3.util.ssl_.TLSVersion('TLSv1')
