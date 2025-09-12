import urllib3

# Create a custom SSL context with platform-native TLS
http = urllib3.PoolManager(
    ssl_context=urllib3.ssl_support_code.get_native_context(),
)

# Now you can use the http object to make HTTPS requests
response = http.request('GET', 'https://example.com')
print(response.data.decode())
