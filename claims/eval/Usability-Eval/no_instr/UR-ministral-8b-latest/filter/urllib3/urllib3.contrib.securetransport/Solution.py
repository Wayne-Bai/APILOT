import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create an SSL context using platform-native TLS
ssl_context = create_urllib3_context()

# Create a pool manager with the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Example usage
response = http.request("GET", "https://example.com")
print(response.data)
