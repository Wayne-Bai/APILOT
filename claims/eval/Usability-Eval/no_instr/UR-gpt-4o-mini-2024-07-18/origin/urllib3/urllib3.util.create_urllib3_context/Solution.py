import urllib3
import ssl

# Create and configure an SSLContext instance
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Create a PoolManager with the SSLContext
http = urllib3.PoolManager(ssl=ssl_context)

# Example request using the configured PoolManager
response = http.request('GET', 'https://example.com')
print(response.data)
