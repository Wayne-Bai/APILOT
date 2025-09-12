import urllib3
import ssl

# Create a default SSL context that enables hostname checking
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED  # or ssl.CERT_OPTIONAL based on your requirement

# The server_hostname parameter is required for hostname verification
server_hostname = 'your.server.com'  # Replace with the actual server hostname

# Create a PoolManager with the custom SSL context
http = urllib3.PoolManager(ssl_context=context)

# Making a request while ensuring host verification
response = http.request('GET', f'https://{server_hostname}')

# Output the response data
print(response.data)
