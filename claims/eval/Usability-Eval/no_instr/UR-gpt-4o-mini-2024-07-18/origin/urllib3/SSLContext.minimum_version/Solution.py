import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Define the minimum supported version
MINIMUM_SUPPORTED_VERSION = 'TLSv1.2'

# Create a custom context with the minimum version set
context = create_urllib3_context(minimum_version=MINIMUM_SUPPORTED_VERSION)

# Create a PoolManager with this context
http = urllib3.PoolManager(ssl=context)

# Example usage: Making a request
response = http.request('GET', 'https://example.com')
print(response.data)
