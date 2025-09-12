
import urllib3
from urllib3.contrib import pyopenssl

# Create a pool manager with the lowest supported version of TLS
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ssl_version=pyopenssl.constants.TLSVersion.MINIMUM_SUPPORTED
)

# Example usage
response = http.request('GET', 'https://example.com')
print(response.status)
