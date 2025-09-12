import urllib3
import pyopenssl

# Create a new SSL context using pyOpenSSL
ssl_context = pyopenssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Set the certificate and key for the SSL context
ssl_context.load_certificate('path/to/your/certificate.pem')
ssl_context.load_privatekey('path/to/your/private_key.pem', 'password')

# Create a new HTTPSConnection using the SSL context
https = urllib3.HTTPSConnection(host='www.example.com', port=443, ssl_context=ssl_context)

# Make an HTTP GET request to the server
response = https.request('GET', '/')

# Print the response status and headers
print(response.status, response.headers)
