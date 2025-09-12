import urllib3

# Create a PoolManager instance with TLS (SSL) support
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs='/path/to/cacert.pem')

# Make a secure GET request to a site
response = http.request('GET', 'https://example.com')

# Print the response data
print("Response status:", response.status)
print("Response body:", response.data.decode('utf-8'))

# Close the connection
response.release_conn()
