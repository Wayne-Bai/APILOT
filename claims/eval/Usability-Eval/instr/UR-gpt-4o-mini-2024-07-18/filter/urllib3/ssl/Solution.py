import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Creating a default SSL context for secure connections
ssl_context = create_urllib3_context()

# Create a PoolManager with the SSL context
http = urllib3.PoolManager(ssl=ssl_context)

# Example of making a secure GET request
url = 'https://example.com'
response = http.request('GET', url)

print(f'Status: {response.status}')
print(f'Body: {response.data.decode("utf-8")}')
