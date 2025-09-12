import urllib3
from urllib3.util.ssl_ import SSLContext, PROTOCOL_TLS_CLIENT, CERT_NONE
from ssl import TLSVersion

# Create an SSL context
ssl_context = SSLContext(PROTOCOL_TLS_CLIENT)

# Set the minimum supported TLS version
ssl_context.minimum_version = TLSVersion.TLSv1_2

# Make a connection using urllib3 with the configured SSL context
http = urllib3.PoolManager(ssl_context=ssl_context, cert_reqs=CERT_NONE)

# Example: GET request
response = http.request('GET', 'https://www.example.com')
print(response.data.decode('utf-8'))
