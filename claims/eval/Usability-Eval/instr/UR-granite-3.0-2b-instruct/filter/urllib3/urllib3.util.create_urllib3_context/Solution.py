import urllib3

# Create an SSL context
ssl_context = urllib3.SSLContext(ssl.PROTOCOL_TLSv1)

# Add server certificate (replace 'server_certificate.crt' with your server certificate file)
ssl_context.load_cert_chain('server_certificate.crt', 'server_private_key.key')

# Set the SSL context for the HTTP client
http = urllib3.PoolManager(ssl_context=ssl_context)
