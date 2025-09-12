
import urllib3
import requests
from requests_ntlm import HttpNtlmAuth

http = urllib3.PoolManager()
url = 'http://example.com'

# Define the username and password for the NTLM authentication
username = 'my_username'
password = 'my_password'

# Make a request with the NTLM authentication
response = requests.get(url, auth=HttpNtlmAuth(username, password), pool_manager=http)

# Print the response
print(response.status_code)
print(response.text)

