import urllib3

# Create a PoolManager instance for making requests
http = urllib3.PoolManager()

# Example of a secure HTTPS request using TLS
url = 'https://example.com'
response = http.request('GET', url)

# Display the status and data of the response
print(f'Status: {response.status}')
print(f'Data: {response.data.decode("utf-8")}')
