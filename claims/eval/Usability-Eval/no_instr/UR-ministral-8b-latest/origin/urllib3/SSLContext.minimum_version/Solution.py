import urllib3

# Create a custom SSLContext with the minimum version of TLS
ssl_context = urllib3.util.ssl_.ssl.SSLContext().minimum_version(up_ssl_context=urllib3.util.ssl_.make_default_handshake_context())

# Example: Create an HTTP client with the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Make a request (for demonstration purposes)
response = http.request('GET', 'https://www.example.com')
print(response.data)
