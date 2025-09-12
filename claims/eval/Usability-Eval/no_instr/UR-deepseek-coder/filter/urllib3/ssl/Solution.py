import urllib3
import ssl

# Create a pool manager with SSL context
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate.pem',
    ssl_version=ssl.PROTOCOL_TLSv1_2
)

# Example request
try:
    response = http.request('GET', 'https://example.com')
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
