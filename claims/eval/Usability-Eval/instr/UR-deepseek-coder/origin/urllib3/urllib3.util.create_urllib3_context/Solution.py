import urllib3
import ssl

# Create an SSLContext instance
ssl_context = ssl.create_default_context()

# Optionally, configure the SSLContext instance
# For example, to disable SSL certificate verification:
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create a urllib3 PoolManager with the configured SSLContext
http = urllib3.PoolManager(ssl_context=ssl_context)

# Now you can use 'http' to make requests with the configured SSLContext
# Example request:
response = http.request('GET', 'https://example.com')
print(response.data.decode('utf-8'))
