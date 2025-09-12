import urllib3

# Create a pool manager with a specific SSL version
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Require certificate validation
    ca_certs='/path/to/ca_bundle.crt',  # Path to your CA bundle
    ssl_version=urllib3.util.ssl_.PROTOCOL_TLSv1_2  # Specify the SSL version
)

# Example request
try:
    response = http.request('GET', 'https://example.com')
    print(response.status)
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
