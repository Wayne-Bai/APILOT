import ssl
import urllib3

# Create and configure the SSLContext instance
context = ssl.create_default_context()

# Optionally, load a client certificate and key for client-side TLS
context.load_cert_chain(certfile='/path/to/certfile.pem', keyfile='/path/to/keyfile.pem')

# Apply the SSLContext to the PoolManager
http = urllib3.PoolManager(ssl_context=context)

# Example usage to make a GET request
response = http.request('GET', 'https://example.com')
print(response.data.decode('utf-8'))
