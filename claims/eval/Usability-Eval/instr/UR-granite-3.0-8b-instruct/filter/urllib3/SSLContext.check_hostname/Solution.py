import urllib3

# Create a SSL context with hostname verification enabled
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='path/to/ca_cert.pem',  # Replace with the path to your CA certificate
    # Enable hostname verification
    # By default, hostname verification is disabled for the PROTOCOL_TLS_CLIENT protocol
    # You need to enable it explicitly for other protocols
    # For example, for the PROTOCOL_TLS_SERVER protocol:
    # ssl_context=ssl.create_default_context(ssl.Purpose.SERVER_AUTH),
    # ssl_context.check_hostname=True,
    # ssl_context.verify_mode=ssl.CERT_REQUIRED
)

# Use the PoolManager to send a request
response = http.request('GET', 'https://example.com')

# Print the response status code
print(response.status)
