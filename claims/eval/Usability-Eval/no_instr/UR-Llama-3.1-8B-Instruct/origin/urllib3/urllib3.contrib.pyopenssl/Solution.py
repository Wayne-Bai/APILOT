# Import the required module
import ssl

# Import the urllib3 module to use its HTTP client
from urllib3 import PoolManager

# Create a SSL context object with the pyOpenSSL as the TLS backend
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_verify_locations("path_to_ca_cert.pem")  # Load the CA certificate
ssl_context.load_cert_chain("path_to_certificate.pem", "path_to_private_key.pem")

# Create the PoolManager with the SSL context
http = PoolManager(num_pools=10, block=False, retries=5, ssl_context=ssl_context)

# Use the PoolManager to make requests
request = http.request('GET', 'https://example.com')

# Print the request response
print(request.data.decode('utf-8'))
