import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create a custom SSL context using OpenSSL
context = create_urllib3_context()

# Initialize the urllib3 PoolManager with the SSL context
http = urllib3.PoolManager(ssl_context=context)

# Specify the URL to make a secure request
url = 'https://example.com'

# Perform a GET request
response = http.request('GET', url)

# Print the response data
print("Status Code:", response.status)
print("Body:", response.data.decode('utf-8'))

# Clean up resources
response.release_conn()
