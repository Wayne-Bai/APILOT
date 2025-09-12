import urllib3

# Define the lowest supported version of SSL
minimum_version = urllib3.util.ssl_.MinimumVersion.TLSVersion.SSLv3

# Create a SSLContext object with the lowest supported version
context = urllib3.util.ssl_.SSLContext(ssl_version=minimum_version)

# Create a Connecting pool with the SSLContext
http = urllib3.PoolManager(ssl_context=context)

# Now you can make requests using the http object with SSLv3 minimum version
response = http.request('GET', 'https://example.com')
print(response.data)
