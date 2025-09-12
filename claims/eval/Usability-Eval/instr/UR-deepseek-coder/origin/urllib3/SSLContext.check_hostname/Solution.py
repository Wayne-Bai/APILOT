import urllib3
import ssl

# Create a pool manager with a custom SSL context
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Require certificate verification
    ca_certs='/path/to/ca_bundle.pem',  # Path to your CA bundle
    ssl_context=ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
)

# Define the server hostname
server_hostname = 'example.com'

# Make a request to the server
try:
    response = http.request(
        'GET',
        f'https://{server_hostname}',
        headers={'Host': server_hostname},
        assert_hostname=server_hostname
    )
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except urllib3.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
