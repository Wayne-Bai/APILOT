import urllib3

http = urllib3.PoolManager()

# Make a request to a website
response = http.request('GET', 'https://example.com')

# Get the header value
header_value = response.getheader('Header-Name')

print(header_value)
