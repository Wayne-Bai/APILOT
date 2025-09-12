import urllib3
from urllib3.contrib import securetransport

# Use SecureTransport SSL
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=securetransport.extract_from_system()
)

# Now you can make HTTP requests as usual and it will use macOS's native TLS
url = "https://httpbin.org/get"
response = http.request('GET', url)
print(response.status)
print(response.data)
