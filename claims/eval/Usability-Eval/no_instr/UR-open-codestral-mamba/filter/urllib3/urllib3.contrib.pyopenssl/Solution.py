import urllib3
from urllib3.util.ssl_ import create_urllib3_context
import ssl

# Create a custom SSL context
ssl_context = create_urllib3_context(ssl.PROTOCOL_TLSv1_2)

# Specify the SNI hostname
ssl_context.set_alpn_protocols(['h2', 'spdy/3', 'http/1.1'])

# Use urllib3 with the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Use http for making requests
response = http.request('GET', 'https://example.com')

print(response.status)
print(response.data)
