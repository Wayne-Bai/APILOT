import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create SSL context for urllib3 that uses platform-native TLS (SecureTransport on macOS)
ssl_context = create_urllib3_context()

# Example of using this context to make a HTTPS request
http = urllib3.PoolManager(ssl_context=ssl_context)

# Target URL
url = 'https://example.com'

# Make the request
response = http.request('GET', url)

# Print the response
print(response.status)
print(response.data.decode('utf-8'))
