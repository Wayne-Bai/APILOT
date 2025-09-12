import urllib3

# Set the lowest supported version to TLS 1.0
lowest_supported_version = urllib3.SSLContext.TLSv1_0

# Create a new SSLContext with the lowest supported version
ssl_context = urllib3.SSLContext()
ssl_context.minimum_version = lowest_supported_version

# Now you can use this ssl_context with urllib3.PoolManager or other urllib3 components
# For example:
http = urllib3.PoolManager(ssl_context=ssl_context)
response = http.request('GET', 'https://example.com')
