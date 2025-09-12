import urllib3
import ssl

# Disable warnings from urllib3
urllib3.disable_warnings()

# Create a new SSL context
ssl_context = ssl.create_default_context()

# Initialize a PoolManager instance with the SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Make a request
response = http.request('GET', 'https://example.com')

# Print the response
print(response.status)
print(response.data)
