import urllib3
import ssl

# Create an SSL context
ssl_context = ssl.create_default_context()

# You can customize the SSL context here if needed
# For example, to set the minimum SSL version
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2

# Create a PoolManager with the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Now you can use the http object to make requests
response = http.request('GET', 'https://example.com')
print(response.data)
