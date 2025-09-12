
import urllib3
from requests_ntlm import HttpNtlmAuth

# Initialize a PoolManager and setup NTLM authentication
http = urllib3.PoolManager()
url = 'https://example.com'
username = 'your_username'
password = 'your_password'
auth = HttpNtlmAuth(username, password)

# Make a request using the authenticated PoolManager
response = http.request('GET', url, auth=auth)

print(response.data)
