import urllib3

# Create a PoolManager with SNI support
http = urllib3.PoolManager()

# URL for the HTTPS request
url = 'https://example.com'

# Make the request
try:
    response = http.request('GET', url)
    print(f'Status: {response.status}')
    print(f'Response data: {response.data.decode("utf-8")}')
except urllib3.exceptions.SSLError as e:
    print(f'SSL Error: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
