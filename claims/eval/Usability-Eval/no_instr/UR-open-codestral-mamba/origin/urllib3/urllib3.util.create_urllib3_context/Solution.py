import urllib3
import ssl

# Create a custom SSL context
ssl_context = ssl.create_default_context()

# Set your SSL certificate verification requirements here
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create a urllib3 PoolManager with your custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Now you can use 'http' for urllib3 requests like this:
r = http.request('GET', 'http://example.com')
