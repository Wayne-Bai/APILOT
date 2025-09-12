
import urllib3

# Disable warnings
urllib3.disable_warnings()

# Create a PoolManager
http = urllib3.PoolManager()

# Send a GET request
response = http.request('GET', 'https://www.example.com')

# Get the value of a specific header
header_value = response.headers.get('header_name')
print(header_value)
