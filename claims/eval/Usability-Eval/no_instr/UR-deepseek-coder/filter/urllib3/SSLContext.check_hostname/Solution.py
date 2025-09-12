import urllib3

# Create a pool manager with SSL/TLS configuration
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Require certificate verification
    ca_certs='path/to/your/ca_bundle.pem',  # Path to your CA bundle file
    assert_hostname=True  # Enable hostname checking
)

# Define the server hostname
server_hostname = 'example.com'

# Make a request to the server
try:
    response = http.request(
        'GET',
        f'https://{server_hostname}',
        headers={'Host': server_hostname}
    )
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except urllib3.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
