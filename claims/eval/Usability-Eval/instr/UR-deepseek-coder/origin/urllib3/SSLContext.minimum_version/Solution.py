import urllib3

# Create a pool manager with the lowest supported TLS version
http = urllib3.PoolManager(
    ssl_context=urllib3.util.ssl_.create_urllib3_context(
        ssl_minimum_version=urllib3.util.ssl_.TLSVersion.MINIMUM_SUPPORTED
    )
)

# Example usage
response = http.request('GET', 'https://example.com')
print(response.data.decode('utf-8'))
