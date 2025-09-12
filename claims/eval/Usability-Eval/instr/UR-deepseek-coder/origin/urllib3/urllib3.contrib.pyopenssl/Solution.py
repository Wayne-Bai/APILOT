import urllib3
import ssl

# Create a custom SSL context with SNI support
context = ssl.create_default_context()

# Create a pool manager with the custom SSL context
http = urllib3.PoolManager(ssl_context=context)

# Example request
response = http.request('GET', 'https://example.com')
print(response.data.decode('utf-8'))
