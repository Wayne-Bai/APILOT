import urllib3

# Ensure that we create a connection pool with platform-native TLS on macOS
http = urllib3.PoolManager()

# Example of making a request
response = http.request('GET', 'https://www.example.com')

# Print the status and data of the response
print(f'Status: {response.status}')
print(f'Data: {response.data.decode("utf-8")}')
