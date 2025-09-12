import urllib3
import ssl

# Create a SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Set the verify mode to CERT_REQUIRED
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Specify the hostname for verification
hostname = 'example.com'

# Create a PoolManager with the SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Make a request to the server
response = http.request('GET', f'https://{hostname}')

# Print the response status and data
print(f'Status: {response.status}')
print(f'Data: {response.data.decode("utf-8")}')
