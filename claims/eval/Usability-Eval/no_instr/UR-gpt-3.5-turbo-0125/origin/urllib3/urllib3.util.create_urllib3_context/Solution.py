
import urllib3
import certifi

# Create and configure an SSLContext instance
tls_config = urllib3.util.ssl_.create_urllib3_context()
tls_config.load_default_certs(purpose=ssl.Purpose.SERVER_AUTH)
tls_config.verify_mode = ssl.CERT_REQUIRED
tls_config.check_hostname = True

# Configure the SSLContext instance with the trust roots
tls_config.load_verify_locations(cafile=certifi.where())
