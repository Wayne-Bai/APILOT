import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Optional: Customizing SSL/TLS settings
# This context uses the default settings provided by the urllib3.
ssl_context = create_urllib3_context()

http = urllib3.PoolManager(ssl_context=ssl_context)

# Example GET request
url = 'https://example.com'
response = http.request('GET', url)

print(response.status)
print(response.data.decode('utf-8'))
