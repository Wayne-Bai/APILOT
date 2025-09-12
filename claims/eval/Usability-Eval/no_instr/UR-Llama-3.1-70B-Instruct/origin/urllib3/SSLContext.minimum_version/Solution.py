# Import required libraries
import ssl
import urllib3

# Create a custom SSL context with the lowest supported TLS version
context = ssl.create_default_context()
context.options &= ~ssl.OP_NO_TLSv1
context.options &= ~ssl.OP_NO_TLSv1_1

# Lowest supported TLS version
lowest_supported = ssl.TLSVersion.TLSv1

# Set the minimum TLS version to the lowest supported
context.minimum_version = lowest_supported

# Create a PoolManager with the custom SSL context
http = urllib3.PoolManager(
    ssl_context=context
)

# Usage example
try:
    response = http.request('GET', 'https://httpbin.org/ip')
    print(response.status)
except urllib3.exceptions.MaxRetryError as e:
    print(f"Failed to connect: {e}")
except urllib3.exceptions.SSLError as e:
    print(f"SSL error: {e}")
