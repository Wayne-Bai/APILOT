import urllib3

# Create a pool manager instance
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs='/path/to/your/certificate.crt')

# Define the URL you want to access
url = 'https://example.com'

# Make a request to the URL
response = http.request('GET', url)

# Print the response status and data
print(f"Response status: {response.status}")
print(f"Response data: {response.data.decode('utf-8')}")
