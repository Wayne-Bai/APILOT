import urllib3
import ssl
import certifi

# Create a PoolManager with SSL context
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certificate Authority bundle.
    ssl_version=ssl.PROTOCOL_TLSv1_2  # Use TLS v1.2 protocol
)

# Example: Send a GET request
try:
    response = http.request('GET', 'https://www.example.com')
    print(response.status)
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
