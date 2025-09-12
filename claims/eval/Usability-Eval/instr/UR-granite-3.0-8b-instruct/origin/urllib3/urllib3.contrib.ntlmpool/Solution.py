import urllib3

# Create an HTTP connection pool with NTLM authentication
http = urllib3.PoolManager(
    maxsize=10,  # Maximum number of connections in the pool
    disable_reputation=True,
    disable_warnings=True,
    auth_handler=urllib3.auth.NTLMAuthHandler('username', 'password'),  # Replace 'username' and 'password' with your actual credentials
)

# Use the pool to send a GET request
response = http.request('GET', 'http://example.com')

# Print the response status code and content
print(f'Status code: {response.status}')
print(f'Content: {response.data.decode()}')
