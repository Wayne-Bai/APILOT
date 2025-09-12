
# Importing urllib3
import urllib3

# Create a connection pool manager for Google App Engine sandbox applications
manager = urllib3.PoolManager()

# Make a request using the connection pool manager
response = manager.request('GET', 'http://example.com')

# Print the response status code and data
print('Status code:', response.status)
print('Response data:', response.data)
