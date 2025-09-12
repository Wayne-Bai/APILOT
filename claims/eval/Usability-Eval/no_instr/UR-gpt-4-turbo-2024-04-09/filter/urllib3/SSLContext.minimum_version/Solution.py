import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create an SSL context specifying the minimum supported TLS version
ssl_context = create_urllib3_context()

# Explicitly set the minimum supported TLS version (adjust as needed)
ssl_context.minimum_version = ssl_context.TLSVersion.TLSv1_2

# Create a PoolManager with the custom context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Example request using the configured minimum TLS version
response = http.request('GET', 'https://example.com')
print(response.status)
print(response.data.decode('utf-8'))
