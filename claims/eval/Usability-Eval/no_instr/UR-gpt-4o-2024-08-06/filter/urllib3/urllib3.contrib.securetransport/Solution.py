import urllib3
import certifi

# Create a PoolManager instance with platform-native TLS using certifi
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',     # Enforce certificate validation
    ca_certs=certifi.where()       # Path to the Certificate Authority certificates
)

# Usage example: making an HTTPS request
url = "https://www.example.com"
response = http.request('GET', url)

# Print the status and data
print(f"Status: {response.status}")
print(f"Data: {response.data.decode('utf-8')}")
