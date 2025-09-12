
import urllib3
from OpenSSL import SSL

# Create a new SSL context using pyOpenSSL
ctx = SSL.Context(SSL.TLSv1_METHOD)

# Set the certificate and key for the context
ctx.use_certificate('path/to/certificate.pem')
ctx.use_privatekey('path/to/key.pem')

# Create a new HTTPS connection using urllib3
https = urllib3.PoolManager(num_pools=2, certificate_chain=ctx)

# Make an HTTPS request to the URL
response = https.request('GET', 'https://www.example.com/')

# Print the response status code and headers
print(response.status)
print(response.headers)
