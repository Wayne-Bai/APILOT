import requests
import urllib3
from requests.auth import HTTPDigestAuth, HTTPNTLM

# Create a connection pool manager
http = urllib3.PoolManager()

# Create a response object using the connection pool
url = 'https://example.com'
username = 'username'
password = 'password'

# Configure the appropriate authentication method
auth = HTTPNTLM(username, password)

# Send a request to the URL
response = http.request('GET', url, auth=auth)

# Use the data from the response as needed
print(response.data)
