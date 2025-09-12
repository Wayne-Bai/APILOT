import urllib3

# Create a pool manager with the desired SSL version
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Require SSL certificate
    ca_certs='/path/to/ca_bundle.crt',  # Path to the CA bundle
    ssl_version=urllib3.util.ssl_.PROTOCOL_TLSv1_2  # Specify the SSL version
)

# Example URL to test
url = 'https://example.com'

try:
    # Make a request to the server
    response = http.request('GET', url)
    print(f"Response status: {response.status}")
    print(f"Response data: {response.data.decode('utf-8')}")
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
