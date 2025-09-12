import urllib3
import ssl
import platform

# Check the platform
if platform.system() == "Darwin":
    # For macOS, we need to set the OpenSSL library location manually and create a ssl context
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers('DEFAULT:!aNULL:!eNULL:!MD5:!3DES:!DES')
    http = urllib3.PoolManager(ssl_context=ssl_context)
else:
    # For other platforms, we can use the default settings
    http = urllib3.PoolManager()

# Now, you can use the 'http' object to make requests
response = http.request('GET', 'https://example.com')
print(response.data)
