import urllib3
import logging

# Setup logging for debug information
logging.basicConfig(level=logging.DEBUG)

# Create a PoolManager instance using pyOpenSSL as the SSL context
http = urllib3.PoolManager()

# Making a HTTPS request using the PoolManager
url = "https://example.com"
response = http.request('GET', url)

# Print out the response data
print(response.data.decode('utf-8'))
