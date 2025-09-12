
import urllib3

# Disable warnings
urllib3.disable_warnings()

URL = 'https://httpbin.org/get'
http = urllib3.PoolManager()

response = http.request('GET', URL)

header_value = response.headers.get('header_name', 'default_value')
print(f'Header value: {header_value}')
