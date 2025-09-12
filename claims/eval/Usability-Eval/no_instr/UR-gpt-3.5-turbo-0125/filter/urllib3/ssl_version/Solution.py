
import urllib3

# Create a custom SSL context to specify the supported SSL versions
context = urllib3.create_urllib3_context(ssl_version=ssl.PROTOCOL_TLSv1_2)

# Use the custom SSL context with an HTTP connection pool
http = urllib3.PoolManager(ssl_context=context)

# Make a request using the custom SSL context
response = http.request('GET', 'https://example.com')

print(response.data.decode('utf-8'))
