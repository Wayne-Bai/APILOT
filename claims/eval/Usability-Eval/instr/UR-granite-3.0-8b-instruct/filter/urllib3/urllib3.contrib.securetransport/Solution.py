import urllib3

# Create a custom TLS context
tls_context = urllib3.TlsContext(ca_certs='/path/to/ca_cert.pem')

# Create a custom HTTP connection pool
http = urllib3.PoolManager(tls_context=tls_context)

# Use the custom HTTP connection pool to make a request
response = http.request('GET', 'https://example.com')

# Print the response
print(response.data.decode())
