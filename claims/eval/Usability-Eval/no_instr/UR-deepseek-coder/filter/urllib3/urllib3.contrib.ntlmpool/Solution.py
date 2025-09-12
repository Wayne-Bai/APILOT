import urllib3
from urllib3.auth import HTTPNtlmAuth

# Create a pool manager with NTLM authentication
http = urllib3.PoolManager(
    auth_class=HTTPNtlmAuth,
    auth=('DOMAIN\\username', 'password')
)

# Example request
response = http.request('GET', 'https://example.com/resource')

# Print the response status and data
print(f"Response status: {response.status}")
print(f"Response data: {response.data.decode('utf-8')}")
