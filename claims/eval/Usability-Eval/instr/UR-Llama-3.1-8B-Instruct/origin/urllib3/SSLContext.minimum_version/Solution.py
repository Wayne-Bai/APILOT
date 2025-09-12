import importlib
import urllib3
import ssl
import ssl.version_selector

# Find the minimum TLS version supported by Python's ssl library
min_tls_version = ssl.version_selector.supported_versions()
min_tls_version = min(min_tls_version)

# Check the minimum TLS version
print(f'The minimum TLS version supported by Python is: {min_tls_version}')

# To set the lowest supported TLS version in an ssl.SSLContext context
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Find the minimum TLS version supported by your Python's ssl library
min_tls_version = ssl.version_selector.supported_versions()
min_tls_version = min(min_tls_version)

# Set the minimum supported version in the SSL context
ssl_context.minimum_version = min_tls_version

#Check the minimum supported version
print(f'The minimum TLS version set in the SSL context is: {min_tls_version}')

# Create an HTTP connection with the SSL context
http = urllib3.PoolManager(cert_reqs=ssl.CERT_REQUIRED, ca_certs=None, ssl_version=min_tls_version)

# Send an HTTP request
response = http.request('GET', 'https://www.google.com')

# Check the status code of the response
print(f'Status code: {response.status}')
