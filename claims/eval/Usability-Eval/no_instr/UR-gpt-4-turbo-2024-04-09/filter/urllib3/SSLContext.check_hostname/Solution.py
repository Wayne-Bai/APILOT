import urllib3
import ssl

# Create a new HTTPS connection pool manager.
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Ensures that the cert is required
    ssl_version=ssl.PROTOCOL_TLS_CLIENT,  # Uses TLS client protocol which has hostname checking enabled by default
    # Here you need to specify the CA bundle if it's not in the default location that urllib3 searches:
    ca_certs='/path/to/your/certificate/bundle.pem'
)

# Make a request to a secure URL
response = http.request('GET', 'https://example.com')

# Print response data
print(response.status)
print(response.data)
