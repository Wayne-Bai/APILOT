import urllib3

# Disable warnings about verifying SSL certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a PoolManager object with TLS verification enabled
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=None)

# Send a GET request
response = http.request('GET', 'https://example.com')

# Print the response status
print(response.status)
