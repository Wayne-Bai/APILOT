import urllib3

# Create a pool manager with platform-native TLS support on macOS
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Ensure certificates are verified
    ca_certs='/path/to/ca_bundle.crt'  # Path to your CA bundle file
)

# Example request
try:
    response = http.request('GET', 'https://example.com')
    print(response.status)
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except urllib3.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
